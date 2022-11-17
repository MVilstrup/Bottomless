from enum import Enum, unique

from bottomless.api.errors.plugins import UnhandledPluginRunTimeErrorState
from bottomless.api.errors.signal_errors import RunTimeCircleCompleted


@unique
class RuntimeState(Enum):
    INITIATED = "INITIATED"
    VALIDATION = "VALIDATE"
    TEST = "TEST"
    SETUP = "SETUP"
    RUN = "RUN"
    SHUTDOWN = "SHUTDOWN"
    CLEANUP = "CLEANUP"
    CLOSE = "CLOSE"
    ERROR = "ERROR"

    @property
    def next(self) -> 'RuntimeState':
        if self.value == RuntimeState.INITIATED.value:
            return RuntimeState.VALIDATION
        elif self.value == RuntimeState.VALIDATION.value:
            return RuntimeState.TEST
        elif self.value == RuntimeState.TEST.value:
            return RuntimeState.SETUP
        elif self.value == RuntimeState.SETUP.value:
            return RuntimeState.RUN
        elif self.value == RuntimeState.RUN.value:
            return RuntimeState.SHUTDOWN
        elif self.value == RuntimeState.SHUTDOWN.value:
            return RuntimeState.CLEANUP
        elif self.value == RuntimeState.CLEANUP.value:
            return RuntimeState.CLOSE
        elif self.value == RuntimeState.CLOSE.value:
            raise RunTimeCircleCompleted("Plugin State is fully closed and ready to shutdown")
        else:
            raise UnhandledPluginRunTimeErrorState("Plugin Reached Unhandled Error State")
