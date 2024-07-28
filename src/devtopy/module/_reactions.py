from typing import List, Optional, Union, TYPE_CHECKING

from ..model import User, UserList, ErrorResponse
from ..exception import DotDevApiError


if TYPE_CHECKING:
    from .._devtopy import DevTo


class Comments:

    def __init__(self, parent: "DevTo"):
        self.parent = parent
