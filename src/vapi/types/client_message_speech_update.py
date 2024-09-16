# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
from .client_message_speech_update_status import ClientMessageSpeechUpdateStatus
import pydantic
from .client_message_speech_update_role import ClientMessageSpeechUpdateRole
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class ClientMessageSpeechUpdate(UniversalBaseModel):
    status: ClientMessageSpeechUpdateStatus = pydantic.Field()
    """
    This is the status of the speech update.
    """

    role: ClientMessageSpeechUpdateRole = pydantic.Field()
    """
    This is the role which the speech update is for.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
