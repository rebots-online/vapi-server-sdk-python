# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations
from ..core.pydantic_utilities import UniversalBaseModel
from .callback_step import CallbackStep
from .create_workflow_block_dto import CreateWorkflowBlockDto
from .handoff_step import HandoffStep
import typing
from .open_ai_message import OpenAiMessage
import pydantic
from .vapi_model_tools_item import VapiModelToolsItem
import typing_extensions
from ..core.serialization import FieldMetadata
from .vapi_model_steps_item import VapiModelStepsItem
from .knowledge_base import KnowledgeBase
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.pydantic_utilities import update_forward_refs


class VapiModel(UniversalBaseModel):
    messages: typing.Optional[typing.List[OpenAiMessage]] = pydantic.Field(default=None)
    """
    This is the starting state for the conversation.
    """

    tools: typing.Optional[typing.List[VapiModelToolsItem]] = pydantic.Field(default=None)
    """
    These are the tools that the assistant can use during the call. To use existing tools, use `toolIds`.
    
    Both `tools` and `toolIds` can be used together.
    """

    tool_ids: typing_extensions.Annotated[typing.Optional[typing.List[str]], FieldMetadata(alias="toolIds")] = (
        pydantic.Field(default=None)
    )
    """
    These are the tools that the assistant can use during the call. To use transient tools, use `tools`.
    
    Both `tools` and `toolIds` can be used together.
    """

    steps: typing.Optional[typing.List[VapiModelStepsItem]] = None
    model: str = pydantic.Field()
    """
    This is the name of the model. Ex. cognitivecomputations/dolphin-mixtral-8x7b
    """

    temperature: typing.Optional[float] = pydantic.Field(default=None)
    """
    This is the temperature that will be used for calls. Default is 0 to leverage caching for lower latency.
    """

    knowledge_base: typing_extensions.Annotated[
        typing.Optional[KnowledgeBase], FieldMetadata(alias="knowledgeBase")
    ] = pydantic.Field(default=None)
    """
    These are the options for the knowledge base.
    """

    max_tokens: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="maxTokens")] = pydantic.Field(
        default=None
    )
    """
    This is the max number of tokens that the assistant will be allowed to generate in each turn of the conversation. Default is 250.
    """

    emotion_recognition_enabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="emotionRecognitionEnabled")
    ] = pydantic.Field(default=None)
    """
    This determines whether we detect user's emotion while they speak and send it as an additional info to model.
    
    Default `false` because the model is usually are good at understanding the user's emotion from text.
    
    @default false
    """

    num_fast_turns: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="numFastTurns")] = (
        pydantic.Field(default=None)
    )
    """
    This sets how many turns at the start of the conversation to use a smaller, faster model from the same provider before switching to the primary model. Example, gpt-3.5-turbo if provider is openai.
    
    Default is 0.
    
    @default 0
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(CallbackStep, VapiModel=VapiModel)
update_forward_refs(CreateWorkflowBlockDto, VapiModel=VapiModel)
update_forward_refs(HandoffStep, VapiModel=VapiModel)
