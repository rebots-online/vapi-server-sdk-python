# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
from .sip_trunk_gateway import SipTrunkGateway
import typing_extensions
from .sip_trunk_outbound_authentication_plan import SipTrunkOutboundAuthenticationPlan
from ..core.serialization import FieldMetadata
from .sbc_configuration import SbcConfiguration
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class UpdateByoSipTrunkCredentialDto(UniversalBaseModel):
    provider: typing.Optional[typing.Literal["byo-sip-trunk"]] = pydantic.Field(default=None)
    """
    This can be used to bring your own SIP trunks or to connect to a Carrier.
    """

    gateways: typing.List[SipTrunkGateway] = pydantic.Field()
    """
    This is the list of SIP trunk's gateways.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the name of the SIP trunk. This is just for your reference.
    """

    outbound_authentication_plan: typing_extensions.Annotated[
        typing.Optional[SipTrunkOutboundAuthenticationPlan], FieldMetadata(alias="outboundAuthenticationPlan")
    ] = pydantic.Field(default=None)
    """
    This can be used to configure the outbound authentication if required by the SIP trunk.
    """

    outbound_leading_plus_enabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="outboundLeadingPlusEnabled")
    ] = pydantic.Field(default=None)
    """
    This ensures the outbound origination attempts have a leading plus. Defaults to false to match conventional telecom behavior.
    
    Usage:
    
    - Vonage/Twilio requires leading plus for all outbound calls. Set this to true.
    
    @default false
    """

    sbc_configuration: typing_extensions.Annotated[
        typing.Optional[SbcConfiguration], FieldMetadata(alias="sbcConfiguration")
    ] = pydantic.Field(default=None)
    """
    This is an advanced configuration for enterprise deployments. This uses the onprem SBC to trunk into the SIP trunk's `gateways`, rather than the managed SBC provided by Vapi.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
