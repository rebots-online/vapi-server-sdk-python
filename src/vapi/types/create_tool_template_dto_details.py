# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.pydantic_utilities import UniversalBaseModel
import typing
import typing_extensions
from ..core.serialization import FieldMetadata
from .create_dtmf_tool_dto_messages_item import CreateDtmfToolDtoMessagesItem
from .open_ai_function import OpenAiFunction
from .server import Server
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from .create_end_call_tool_dto_messages_item import CreateEndCallToolDtoMessagesItem
from .create_voicemail_tool_dto_messages_item import CreateVoicemailToolDtoMessagesItem
from .create_function_tool_dto_messages_item import CreateFunctionToolDtoMessagesItem
from .create_ghl_tool_dto_messages_item import CreateGhlToolDtoMessagesItem
from .ghl_tool_metadata import GhlToolMetadata
from .create_make_tool_dto_messages_item import CreateMakeToolDtoMessagesItem
from .make_tool_metadata import MakeToolMetadata
from .create_transfer_call_tool_dto_messages_item import CreateTransferCallToolDtoMessagesItem
from .create_transfer_call_tool_dto_destinations_item import CreateTransferCallToolDtoDestinationsItem


class CreateToolTemplateDtoDetails_Dtmf(UniversalBaseModel):
    type: typing.Literal["dtmf"] = "dtmf"
    async_: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="async")] = None
    messages: typing.Optional[typing.List[CreateDtmfToolDtoMessagesItem]] = None
    function: typing.Optional[OpenAiFunction] = None
    server: typing.Optional[Server] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CreateToolTemplateDtoDetails_EndCall(UniversalBaseModel):
    type: typing.Literal["endCall"] = "endCall"
    async_: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="async")] = None
    messages: typing.Optional[typing.List[CreateEndCallToolDtoMessagesItem]] = None
    function: typing.Optional[OpenAiFunction] = None
    server: typing.Optional[Server] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CreateToolTemplateDtoDetails_Voicemail(UniversalBaseModel):
    type: typing.Literal["voicemail"] = "voicemail"
    async_: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="async")] = None
    messages: typing.Optional[typing.List[CreateVoicemailToolDtoMessagesItem]] = None
    function: typing.Optional[OpenAiFunction] = None
    server: typing.Optional[Server] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CreateToolTemplateDtoDetails_Function(UniversalBaseModel):
    type: typing.Literal["function"] = "function"
    async_: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="async")] = None
    messages: typing.Optional[typing.List[CreateFunctionToolDtoMessagesItem]] = None
    function: typing.Optional[OpenAiFunction] = None
    server: typing.Optional[Server] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CreateToolTemplateDtoDetails_Ghl(UniversalBaseModel):
    type: typing.Literal["ghl"] = "ghl"
    async_: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="async")] = None
    messages: typing.Optional[typing.List[CreateGhlToolDtoMessagesItem]] = None
    metadata: GhlToolMetadata
    function: typing.Optional[OpenAiFunction] = None
    server: typing.Optional[Server] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CreateToolTemplateDtoDetails_Make(UniversalBaseModel):
    type: typing.Literal["make"] = "make"
    async_: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="async")] = None
    messages: typing.Optional[typing.List[CreateMakeToolDtoMessagesItem]] = None
    metadata: MakeToolMetadata
    function: typing.Optional[OpenAiFunction] = None
    server: typing.Optional[Server] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class CreateToolTemplateDtoDetails_TransferCall(UniversalBaseModel):
    type: typing.Literal["transferCall"] = "transferCall"
    async_: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="async")] = None
    messages: typing.Optional[typing.List[CreateTransferCallToolDtoMessagesItem]] = None
    destinations: typing.Optional[typing.List[CreateTransferCallToolDtoDestinationsItem]] = None
    function: typing.Optional[OpenAiFunction] = None
    server: typing.Optional[Server] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


CreateToolTemplateDtoDetails = typing.Union[
    CreateToolTemplateDtoDetails_Dtmf,
    CreateToolTemplateDtoDetails_EndCall,
    CreateToolTemplateDtoDetails_Voicemail,
    CreateToolTemplateDtoDetails_Function,
    CreateToolTemplateDtoDetails_Ghl,
    CreateToolTemplateDtoDetails_Make,
    CreateToolTemplateDtoDetails_TransferCall,
]
