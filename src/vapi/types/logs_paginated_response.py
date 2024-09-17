# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .log import Log
from .pagination_meta import PaginationMeta
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class LogsPaginatedResponse(UniversalBaseModel):
    results: typing.List[Log]
    metadata: PaginationMeta

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow