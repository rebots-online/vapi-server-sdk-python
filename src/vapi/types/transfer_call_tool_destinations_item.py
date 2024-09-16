# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.pydantic_utilities import UniversalBaseModel
import typing
import typing_extensions
from .transfer_destination_assistant_transfer_mode import TransferDestinationAssistantTransferMode
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class TransferCallToolDestinationsItem_Assistant(UniversalBaseModel):
    type: typing.Literal["assistant"] = "assistant"
    transfer_mode: typing_extensions.Annotated[
        typing.Optional[TransferDestinationAssistantTransferMode], FieldMetadata(alias="transferMode")
    ] = None
    assistant_name: typing_extensions.Annotated[str, FieldMetadata(alias="assistantName")]
    message: typing.Optional[str] = None
    description: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransferCallToolDestinationsItem_Step(UniversalBaseModel):
    type: typing.Literal["step"] = "step"
    step_name: typing_extensions.Annotated[str, FieldMetadata(alias="stepName")]
    message: typing.Optional[str] = None
    description: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransferCallToolDestinationsItem_Number(UniversalBaseModel):
    type: typing.Literal["number"] = "number"
    number_e_164_check_enabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="numberE164CheckEnabled")
    ] = None
    number: str
    extension: typing.Optional[str] = None
    caller_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="callerId")] = None
    message: typing.Optional[str] = None
    description: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class TransferCallToolDestinationsItem_Sip(UniversalBaseModel):
    type: typing.Literal["sip"] = "sip"
    sip_uri: typing_extensions.Annotated[str, FieldMetadata(alias="sipUri")]
    message: typing.Optional[str] = None
    description: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


TransferCallToolDestinationsItem = typing.Union[
    TransferCallToolDestinationsItem_Assistant,
    TransferCallToolDestinationsItem_Step,
    TransferCallToolDestinationsItem_Number,
    TransferCallToolDestinationsItem_Sip,
]
