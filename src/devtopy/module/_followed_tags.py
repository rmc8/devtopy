from typing import Union, TYPE_CHECKING

from ..model import Tag, TagList, ErrorResponse
from ..exception import DotDevApiError


if TYPE_CHECKING:
    from .._devtopy import DevTo


class FollowedTags:

    def __init__(self, parent: "DevTo"):
        self.parent = parent

    def get(self) -> Union[TagList, ErrorResponse]:
        endpoint = self.parent._build_url("follows/tags")
        res = self.parent._request("GET", endpoint)
        if res.status_code == 200:
            data = res.json()
            tags = [Tag(**tag) for tag in data]
            return TagList(tags=tags)
        elif res.status_code == 401:
            data = res.json()
            return ErrorResponse(**data)
        raise DotDevApiError(response=res)
