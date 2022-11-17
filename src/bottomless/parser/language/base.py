from typing import Any
import re


class BlessElement:
    __slots__ = ["name", "value"]
    token = None
    tag = None
    re = None

    def __int__(self, name: str, value: Any):  # type: ignore
        self.name = name
        self.value = value


def element(token: str, tag: str, multi: bool = False) -> BlessElement:
    def __new_init__(self, name: str, value: Any):  # type: ignore
        super().__init__(self, name, value)  # type: ignore

    # creating class dynamically
    new_type = type(token, (BlessElement,), {
        "token": token,
        "tag": tag,
        "re":  re.compile(tag) if not multi else re.compile(tag, re.MULTILINE)
    })
    new_type.__init__ = __new_init__  # type: ignore
    return new_type  # type: ignore
