# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.pydantic_utilities import UniversalBaseModel
from .callback_step import CallbackStep
from .create_workflow_block_dto import CreateWorkflowBlockDto
from .handoff_step import HandoffStep
import typing
from .call_type import CallType
import pydantic
from .call_costs_item import CallCostsItem
from .call_messages_item import CallMessagesItem
import typing_extensions
from .call_phone_call_provider import CallPhoneCallProvider
from ..core.serialization import FieldMetadata
from .call_phone_call_transport import CallPhoneCallTransport
from .call_status import CallStatus
from .call_ended_reason import CallEndedReason
from .call_destination import CallDestination
import datetime as dt
from .cost_breakdown import CostBreakdown
from .artifact_plan import ArtifactPlan
from .analysis import Analysis
from .monitor import Monitor
from .artifact import Artifact
from .create_assistant_dto import CreateAssistantDto
from .assistant_overrides import AssistantOverrides
from .create_squad_dto import CreateSquadDto
from .import_twilio_phone_number_dto import ImportTwilioPhoneNumberDto
from .create_customer_dto import CreateCustomerDto
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.pydantic_utilities import update_forward_refs


class Call(UniversalBaseModel):
    type: typing.Optional[CallType] = pydantic.Field(default=None)
    """
    This is the type of call.
    """

    costs: typing.Optional[typing.List[CallCostsItem]] = pydantic.Field(default=None)
    """
    These are the costs of individual components of the call in USD.
    """

    messages: typing.Optional[typing.List[CallMessagesItem]] = None
    phone_call_provider: typing_extensions.Annotated[
        typing.Optional[CallPhoneCallProvider], FieldMetadata(alias="phoneCallProvider")
    ] = pydantic.Field(default=None)
    """
    This is the provider of the call.
    
    Only relevant for `outboundPhoneCall` and `inboundPhoneCall` type.
    """

    phone_call_transport: typing_extensions.Annotated[
        typing.Optional[CallPhoneCallTransport], FieldMetadata(alias="phoneCallTransport")
    ] = pydantic.Field(default=None)
    """
    This is the transport of the phone call.
    
    Only relevant for `outboundPhoneCall` and `inboundPhoneCall` type.
    """

    status: typing.Optional[CallStatus] = pydantic.Field(default=None)
    """
    This is the status of the call.
    """

    ended_reason: typing_extensions.Annotated[typing.Optional[CallEndedReason], FieldMetadata(alias="endedReason")] = (
        pydantic.Field(default=None)
    )
    """
    This is the explanation for how the call ended.
    """

    destination: typing.Optional[CallDestination] = pydantic.Field(default=None)
    """
    This is the destination where the call ended up being transferred to. If the call was not transferred, this will be empty.
    """

    id: str = pydantic.Field()
    """
    This is the unique identifier for the call.
    """

    org_id: typing_extensions.Annotated[str, FieldMetadata(alias="orgId")] = pydantic.Field()
    """
    This is the unique identifier for the org that this call belongs to.
    """

    created_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="createdAt")] = pydantic.Field()
    """
    This is the ISO 8601 date-time string of when the call was created.
    """

    updated_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="updatedAt")] = pydantic.Field()
    """
    This is the ISO 8601 date-time string of when the call was last updated.
    """

    started_at: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="startedAt")] = (
        pydantic.Field(default=None)
    )
    """
    This is the ISO 8601 date-time string of when the call was started.
    """

    ended_at: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="endedAt")] = (
        pydantic.Field(default=None)
    )
    """
    This is the ISO 8601 date-time string of when the call was ended.
    """

    cost: typing.Optional[float] = pydantic.Field(default=None)
    """
    This is the cost of the call in USD.
    """

    cost_breakdown: typing_extensions.Annotated[
        typing.Optional[CostBreakdown], FieldMetadata(alias="costBreakdown")
    ] = pydantic.Field(default=None)
    """
    This is the cost of the call in USD.
    """

    artifact_plan: typing_extensions.Annotated[typing.Optional[ArtifactPlan], FieldMetadata(alias="artifactPlan")] = (
        pydantic.Field(default=None)
    )
    """
    This is a copy of assistant artifact plan. This isn't actually stored on the call but rather just returned in POST /call/web to enable artifact creation client side.
    """

    analysis: typing.Optional[Analysis] = pydantic.Field(default=None)
    """
    This is the analysis of the call. Configure in `assistant.analysisPlan`.
    """

    monitor: typing.Optional[Monitor] = pydantic.Field(default=None)
    """
    This is to real-time monitor the call. Configure in `assistant.monitorPlan`.
    """

    artifact: typing.Optional[Artifact] = pydantic.Field(default=None)
    """
    These are the artifacts created from the call. Configure in `assistant.artifactPlan`.
    """

    phone_call_provider_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="phoneCallProviderId")
    ] = pydantic.Field(default=None)
    """
    The ID of the call as provided by the phone number service. callSid in Twilio. conversationUuid in Vonage.
    
    Only relevant for `outboundPhoneCall` and `inboundPhoneCall` type.
    """

    assistant_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="assistantId")] = (
        pydantic.Field(default=None)
    )
    """
    This is the assistant that will be used for the call. To use a transient assistant, use `assistant` instead.
    """

    assistant: typing.Optional[CreateAssistantDto] = pydantic.Field(default=None)
    """
    This is the assistant that will be used for the call. To use an existing assistant, use `assistantId` instead.
    """

    assistant_overrides: typing_extensions.Annotated[
        typing.Optional[AssistantOverrides], FieldMetadata(alias="assistantOverrides")
    ] = pydantic.Field(default=None)
    """
    These are the overrides for the `assistant` or `assistantId`'s settings and template variables.
    """

    squad_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="squadId")] = pydantic.Field(
        default=None
    )
    """
    This is the squad that will be used for the call. To use a transient squad, use `squad` instead.
    """

    squad: typing.Optional[CreateSquadDto] = pydantic.Field(default=None)
    """
    This is a squad that will be used for the call. To use an existing squad, use `squadId` instead.
    """

    phone_number_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="phoneNumberId")] = (
        pydantic.Field(default=None)
    )
    """
    This is the phone number that will be used for the call. To use a transient number, use `phoneNumber` instead.
    
    Only relevant for `outboundPhoneCall` and `inboundPhoneCall` type.
    """

    phone_number: typing_extensions.Annotated[
        typing.Optional[ImportTwilioPhoneNumberDto], FieldMetadata(alias="phoneNumber")
    ] = pydantic.Field(default=None)
    """
    This is the phone number that will be used for the call. To use an existing number, use `phoneNumberId` instead.
    
    Only relevant for `outboundPhoneCall` and `inboundPhoneCall` type.
    """

    customer_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="customerId")] = pydantic.Field(
        default=None
    )
    """
    This is the customer that will be called. To call a transient customer , use `customer` instead.
    
    Only relevant for `outboundPhoneCall` and `inboundPhoneCall` type.
    """

    customer: typing.Optional[CreateCustomerDto] = pydantic.Field(default=None)
    """
    This is the customer that will be called. To call an existing customer, use `customerId` instead.
    
    Only relevant for `outboundPhoneCall` and `inboundPhoneCall` type.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the name of the call. This is just for your own reference.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(CallbackStep, Call=Call)
update_forward_refs(CreateWorkflowBlockDto, Call=Call)
update_forward_refs(HandoffStep, Call=Call)