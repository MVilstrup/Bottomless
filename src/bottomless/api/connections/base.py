from typing import Any

from bottomless.api.config.configuration import Configuration
from bottomless.api.config.requirement import ConfigRequirement


class Connection:

    @property
    def requirements(self) -> ConfigRequirement:
        raise NotImplementedError()

    def validate(self, config: Configuration) -> bool:
        raise NotImplementedError()

    def test(self, config: Configuration) -> bool:
        raise NotImplementedError()

    def setup(self, config: Configuration) -> bool:
        raise NotImplementedError()

    def run(self, config: Configuration) -> bool:
        raise NotImplementedError()

    def shutdown(self, config: Configuration) -> bool:
        raise NotImplementedError()

    def cleanup(self, config: Configuration) -> bool:
        raise NotImplementedError()

    def close(self, config: Configuration) -> bool:
        raise NotImplementedError()

    def __enter__(self) -> Any:
        raise NotImplementedError()

    def __exit__(self, exc_type, exc_val, exc_tb):  # type: ignore
        raise NotImplementedError()


