from typing import Union, Tuple


class BluePrint:
    def __init__(self, path: str):
        self._path = path

    def __add__(self, other: 'BluePrint'):
        return self

    def copy(self) -> 'BluePrint':
        return self

    def merge(self, *blueprints: Tuple[Union['BluePrint', str], ...]) -> 'BluePrint':
        return self
