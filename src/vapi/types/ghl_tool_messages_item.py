# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .condition import Condition
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from .tool_message_complete_role import ToolMessageCompleteRole
import typing_extensions
from ..core.serialization import FieldMetadata


class GhlToolMessagesItem_RequestStart(UniversalBaseModel):
    type: typing.Literal["request-start"] = "request-start"
    content: str
    conditions: typing.Optional[typing.List[Condition]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GhlToolMessagesItem_RequestComplete(UniversalBaseModel):
    type: typing.Literal["request-complete"] = "request-complete"
    role: typing.Optional[ToolMessageCompleteRole] = None
    end_call_after_spoken_enabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="endCallAfterSpokenEnabled")
    ] = None
    content: str
    conditions: typing.Optional[typing.List[Condition]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GhlToolMessagesItem_RequestFailed(UniversalBaseModel):
    type: typing.Literal["request-failed"] = "request-failed"
    end_call_after_spoken_enabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="endCallAfterSpokenEnabled")
    ] = None
    content: str
    conditions: typing.Optional[typing.List[Condition]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class GhlToolMessagesItem_RequestResponseDelayed(UniversalBaseModel):
    type: typing.Literal["request-response-delayed"] = "request-response-delayed"
    timing_milliseconds: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="timingMilliseconds")
    ] = None
    content: str
    conditions: typing.Optional[typing.List[Condition]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


GhlToolMessagesItem = typing.Union[
    GhlToolMessagesItem_RequestStart,
    GhlToolMessagesItem_RequestComplete,
    GhlToolMessagesItem_RequestFailed,
    GhlToolMessagesItem_RequestResponseDelayed,
]
