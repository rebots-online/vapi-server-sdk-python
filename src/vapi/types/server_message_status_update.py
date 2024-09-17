# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.pydantic_utilities import UniversalBaseModel
from .callback_step import CallbackStep
from .create_workflow_block_dto import CreateWorkflowBlockDto
from .handoff_step import HandoffStep
import typing_extensions
import typing
from .server_message_status_update_phone_number import ServerMessageStatusUpdatePhoneNumber
from ..core.serialization import FieldMetadata
import pydantic
from .server_message_status_update_status import ServerMessageStatusUpdateStatus
from .server_message_status_update_ended_reason import ServerMessageStatusUpdateEndedReason
from .server_message_status_update_messages_item import ServerMessageStatusUpdateMessagesItem
from .open_ai_message import OpenAiMessage
from .server_message_status_update_destination import ServerMessageStatusUpdateDestination
from .artifact import Artifact
from .create_assistant_dto import CreateAssistantDto
from .create_customer_dto import CreateCustomerDto
from .call import Call
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.pydantic_utilities import update_forward_refs


class ServerMessageStatusUpdate(UniversalBaseModel):
    phone_number: typing_extensions.Annotated[
        typing.Optional[ServerMessageStatusUpdatePhoneNumber], FieldMetadata(alias="phoneNumber")
    ] = pydantic.Field(default=None)
    """
    This is the phone number associated with the call.
    
    This matches one of the following:
    
    - `call.phoneNumber`,
    - `call.phoneNumberId`.
    """

    status: ServerMessageStatusUpdateStatus = pydantic.Field()
    """
    This is the status of the call.
    """

    ended_reason: typing_extensions.Annotated[
        typing.Optional[ServerMessageStatusUpdateEndedReason], FieldMetadata(alias="endedReason")
    ] = pydantic.Field(default=None)
    """
    This is the reason the call ended. This is only sent if the status is "ended".
    """

    messages: typing.Optional[typing.List[ServerMessageStatusUpdateMessagesItem]] = pydantic.Field(default=None)
    """
    These are the conversation messages of the call. This is only sent if the status is "forwarding".
    """

    messages_open_ai_formatted: typing_extensions.Annotated[
        typing.Optional[typing.List[OpenAiMessage]], FieldMetadata(alias="messagesOpenAIFormatted")
    ] = pydantic.Field(default=None)
    """
    These are the conversation messages of the call. This is only sent if the status is "forwarding".
    """

    destination: typing.Optional[ServerMessageStatusUpdateDestination] = pydantic.Field(default=None)
    """
    This is the destination the call is being transferred to. This is only sent if the status is "forwarding".
    """

    timestamp: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the ISO-8601 formatted timestamp of when the message was sent.
    """

    artifact: typing.Optional[Artifact] = pydantic.Field(default=None)
    """
    This is a live version of the `call.artifact`.
    
    This matches what is stored on `call.artifact` after the call.
    """

    assistant: typing.Optional[CreateAssistantDto] = pydantic.Field(default=None)
    """
    This is the assistant that is currently active. This is provided for convenience.
    
    This matches one of the following:
    
    - `call.assistant`,
    - `call.assistantId`,
    - `call.squad[n].assistant`,
    - `call.squad[n].assistantId`,
    - `call.squadId->[n].assistant`,
    - `call.squadId->[n].assistantId`.
    """

    customer: typing.Optional[CreateCustomerDto] = pydantic.Field(default=None)
    """
    This is the customer associated with the call.
    
    This matches one of the following:
    
    - `call.customer`,
    - `call.customerId`.
    """

    call: typing.Optional[Call] = pydantic.Field(default=None)
    """
    This is the call object.
    
    This matches what was returned in POST /call.
    
    Note: This might get stale during the call. To get the latest call object, especially after the call is ended, use GET /call/:id.
    """

    transcript: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the transcript of the call. This is only sent if the status is "forwarding".
    """

    inbound_phone_call_debugging_artifacts: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]],
        FieldMetadata(alias="inboundPhoneCallDebuggingArtifacts"),
    ] = pydantic.Field(default=None)
    """
    This is the inbound phone call debugging artifacts. This is only sent if the status is "ended" and there was an error accepting the inbound phone call.
    
    This will include any errors related to the "assistant-request" if one was made.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(CallbackStep, ServerMessageStatusUpdate=ServerMessageStatusUpdate)
update_forward_refs(CreateWorkflowBlockDto, ServerMessageStatusUpdate=ServerMessageStatusUpdate)
update_forward_refs(HandoffStep, ServerMessageStatusUpdate=ServerMessageStatusUpdate)