# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ...core.pydantic_utilities import UniversalBaseModel
import typing
import typing_extensions
from ...types.byo_phone_number_fallback_destination import ByoPhoneNumberFallbackDestination
from ...core.serialization import FieldMetadata
import datetime as dt
from ...core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic
from ...types.twilio_phone_number_fallback_destination import TwilioPhoneNumberFallbackDestination
from ...types.vonage_phone_number_fallback_destination import VonagePhoneNumberFallbackDestination
from ...types.vapi_phone_number_fallback_destination import VapiPhoneNumberFallbackDestination


class PhoneNumbersListResponseItem_ByoPhoneNumber(UniversalBaseModel):
    provider: typing.Literal["byo-phone-number"] = "byo-phone-number"
    fallback_destination: typing_extensions.Annotated[
        typing.Optional[ByoPhoneNumberFallbackDestination], FieldMetadata(alias="fallbackDestination")
    ] = None
    number_e_164_check_enabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="numberE164CheckEnabled")
    ] = None
    id: str
    org_id: typing_extensions.Annotated[str, FieldMetadata(alias="orgId")]
    created_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="createdAt")]
    updated_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="updatedAt")]
    name: typing.Optional[str] = None
    assistant_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="assistantId")] = None
    squad_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="squadId")] = None
    server_url: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="serverUrl")] = None
    server_url_secret: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="serverUrlSecret")] = None
    number: typing.Optional[str] = None
    credential_id: typing_extensions.Annotated[str, FieldMetadata(alias="credentialId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PhoneNumbersListResponseItem_Twilio(UniversalBaseModel):
    provider: typing.Literal["twilio"] = "twilio"
    fallback_destination: typing_extensions.Annotated[
        typing.Optional[TwilioPhoneNumberFallbackDestination], FieldMetadata(alias="fallbackDestination")
    ] = None
    id: str
    org_id: typing_extensions.Annotated[str, FieldMetadata(alias="orgId")]
    created_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="createdAt")]
    updated_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="updatedAt")]
    name: typing.Optional[str] = None
    assistant_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="assistantId")] = None
    squad_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="squadId")] = None
    server_url: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="serverUrl")] = None
    server_url_secret: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="serverUrlSecret")] = None
    number: str
    twilio_account_sid: typing_extensions.Annotated[str, FieldMetadata(alias="twilioAccountSid")]
    twilio_auth_token: typing_extensions.Annotated[str, FieldMetadata(alias="twilioAuthToken")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PhoneNumbersListResponseItem_Vonage(UniversalBaseModel):
    provider: typing.Literal["vonage"] = "vonage"
    fallback_destination: typing_extensions.Annotated[
        typing.Optional[VonagePhoneNumberFallbackDestination], FieldMetadata(alias="fallbackDestination")
    ] = None
    id: str
    org_id: typing_extensions.Annotated[str, FieldMetadata(alias="orgId")]
    created_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="createdAt")]
    updated_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="updatedAt")]
    name: typing.Optional[str] = None
    assistant_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="assistantId")] = None
    squad_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="squadId")] = None
    server_url: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="serverUrl")] = None
    server_url_secret: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="serverUrlSecret")] = None
    number: str
    credential_id: typing_extensions.Annotated[str, FieldMetadata(alias="credentialId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class PhoneNumbersListResponseItem_Vapi(UniversalBaseModel):
    provider: typing.Literal["vapi"] = "vapi"
    fallback_destination: typing_extensions.Annotated[
        typing.Optional[VapiPhoneNumberFallbackDestination], FieldMetadata(alias="fallbackDestination")
    ] = None
    id: str
    org_id: typing_extensions.Annotated[str, FieldMetadata(alias="orgId")]
    created_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="createdAt")]
    updated_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="updatedAt")]
    name: typing.Optional[str] = None
    assistant_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="assistantId")] = None
    squad_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="squadId")] = None
    server_url: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="serverUrl")] = None
    server_url_secret: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="serverUrlSecret")] = None
    sip_uri: typing_extensions.Annotated[str, FieldMetadata(alias="sipUri")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


PhoneNumbersListResponseItem = typing.Union[
    PhoneNumbersListResponseItem_ByoPhoneNumber,
    PhoneNumbersListResponseItem_Twilio,
    PhoneNumbersListResponseItem_Vonage,
    PhoneNumbersListResponseItem_Vapi,
]
