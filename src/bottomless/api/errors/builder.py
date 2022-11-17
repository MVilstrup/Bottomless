import inspect
from typing import Optional

from bottomless.api.errors.base import BottomlessError


def raise_error(error_type: type, exception: Optional[Exception] = None, msg: Optional[str] = ""):
    func_frame = inspect.getouterframes(inspect.currentframe())[1]

    raise error_type(msg) from exception
