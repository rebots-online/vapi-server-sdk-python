# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.pydantic_utilities import UniversalBaseModel
import typing
import typing_extensions
from .create_byo_phone_number_dto_fallback_destination import CreateByoPhoneNumberDtoFallbackDestination
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from .create_twilio_phone_number_dto_fallback_destination import CreateTwilioPhoneNumberDtoFallbackDestination
from .create_vonage_phone_number_dto_fallback_destination import CreateVonagePhoneNumberDtoFallbackDestination
from .create_vapi_phone_number_dto_fallback_destination import CreateVapiPhoneNumberDtoFallbackDestination


class ServerMessageVoiceInputPhoneNumber_ByoPhoneNumber(UniversalBaseModel):
    """
    This is the phone number associated with the call.

    This matches one of the following:

    - `call.phoneNumber`,
    - `call.phoneNumberId`.
    """

    provider: typing.Literal["byo-phone-number"] = "byo-phone-number"
    fallback_destination: typing_extensions.Annotated[
        typing.Optional[CreateByoPhoneNumberDtoFallbackDestination], FieldMetadata(alias="fallbackDestination")
    ] = None
    number_e_164_check_enabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="numberE164CheckEnabled")
    ] = None
    number: typing.Optional[str] = None
    credential_id: typing_extensions.Annotated[str, FieldMetadata(alias="credentialId")]
    name: typing.Optional[str] = None
    assistant_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="assistantId")] = None
    squad_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="squadId")] = None
    server_url: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="serverUrl")] = None
    server_url_secret: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="serverUrlSecret")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ServerMessageVoiceInputPhoneNumber_Twilio(UniversalBaseModel):
    """
    This is the phone number associated with the call.

    This matches one of the following:

    - `call.phoneNumber`,
    - `call.phoneNumberId`.
    """

    provider: typing.Literal["twilio"] = "twilio"
    fallback_destination: typing_extensions.Annotated[
        typing.Optional[CreateTwilioPhoneNumberDtoFallbackDestination], FieldMetadata(alias="fallbackDestination")
    ] = None
    number: str
    twilio_account_sid: typing_extensions.Annotated[str, FieldMetadata(alias="twilioAccountSid")]
    twilio_auth_token: typing_extensions.Annotated[str, FieldMetadata(alias="twilioAuthToken")]
    name: typing.Optional[str] = None
    assistant_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="assistantId")] = None
    squad_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="squadId")] = None
    server_url: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="serverUrl")] = None
    server_url_secret: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="serverUrlSecret")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ServerMessageVoiceInputPhoneNumber_Vonage(UniversalBaseModel):
    """
    This is the phone number associated with the call.

    This matches one of the following:

    - `call.phoneNumber`,
    - `call.phoneNumberId`.
    """

    provider: typing.Literal["vonage"] = "vonage"
    fallback_destination: typing_extensions.Annotated[
        typing.Optional[CreateVonagePhoneNumberDtoFallbackDestination], FieldMetadata(alias="fallbackDestination")
    ] = None
    number: str
    credential_id: typing_extensions.Annotated[str, FieldMetadata(alias="credentialId")]
    name: typing.Optional[str] = None
    assistant_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="assistantId")] = None
    squad_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="squadId")] = None
    server_url: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="serverUrl")] = None
    server_url_secret: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="serverUrlSecret")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ServerMessageVoiceInputPhoneNumber_Vapi(UniversalBaseModel):
    """
    This is the phone number associated with the call.

    This matches one of the following:

    - `call.phoneNumber`,
    - `call.phoneNumberId`.
    """

    provider: typing.Literal["vapi"] = "vapi"
    fallback_destination: typing_extensions.Annotated[
        typing.Optional[CreateVapiPhoneNumberDtoFallbackDestination], FieldMetadata(alias="fallbackDestination")
    ] = None
    sip_uri: typing_extensions.Annotated[str, FieldMetadata(alias="sipUri")]
    name: typing.Optional[str] = None
    assistant_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="assistantId")] = None
    squad_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="squadId")] = None
    server_url: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="serverUrl")] = None
    server_url_secret: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="serverUrlSecret")] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ServerMessageVoiceInputPhoneNumber = typing.Union[
    ServerMessageVoiceInputPhoneNumber_ByoPhoneNumber,
    ServerMessageVoiceInputPhoneNumber_Twilio,
    ServerMessageVoiceInputPhoneNumber_Vonage,
    ServerMessageVoiceInputPhoneNumber_Vapi,
]
