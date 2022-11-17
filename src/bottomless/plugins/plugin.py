from asyncio import Future
from typing import Tuple, Awaitable

from bottomless.api.config.configuration import Configuration
from bottomless.api.config.requirement import ConfigRequirement
from bottomless.api.enums import RuntimeState
from bottomless.api.errors.plugins import PluginRecoveryError, PluginStateChangeError


class BlessPlugin:

    def __init__(self, force_sequential: bool = False):
        self.state = RuntimeState.INITIATED
        self.sequential = force_sequential

    @property
    def requirements(self) -> ConfigRequirement:
        raise NotImplementedError()

    async def __validate__(self, config: Configuration) -> Awaitable[bool]:
        raise NotImplementedError()

    async def __test__(self, config: Configuration) -> Awaitable[bool]:
        raise NotImplementedError()

    async def __setup__(self, config: Configuration) -> Awaitable[bool]:
        raise NotImplementedError()

    async def __run__(self, config: Configuration) -> Awaitable[bool]:
        raise NotImplementedError()

    async def __shutdown__(self, config: Configuration) -> Awaitable[bool]:
        raise NotImplementedError()

    async def __cleanup__(self, config: Configuration) -> Awaitable[bool]:
        raise NotImplementedError()

    async def __close__(self, config: Configuration) -> Awaitable[bool]:
        raise NotImplementedError()

    def __recover__(self, from_state: RuntimeState, config: Configuration) -> 'BlessPlugin':
        raise NotImplementedError()

    async def next(self, config: Configuration) -> Awaitable[bool]:
        self.state = self.state.next
        if RuntimeState.VALIDATION:
            func = self.__validate__
        elif RuntimeState.TEST:
            func = self.__test__
        elif RuntimeState.SETUP:
            func = self.__setup__
        elif RuntimeState.RUN:
            func = self.__run__
        elif RuntimeState.SHUTDOWN:
            func = self.__shutdown__
        elif RuntimeState.CLEANUP:
            func = self.__cleanup__
        elif RuntimeState.CLOSE:
            func = self.__close__
        else:
            raise build_error(PluginStateChangeError)

        if self.sequential:
            result = await func(config)
            return Future(lambda: result)
        else:
            return func(config)

    def recover(self, from_state: RuntimeState, config: Configuration) -> 'BlessPlugin':
        self.state = RuntimeState.ERROR
        try:
            return self.__recover__(from_state=from_state, config=config)
        except Exception as PRE:
            build_error(PluginRecoveryError, PRE)
