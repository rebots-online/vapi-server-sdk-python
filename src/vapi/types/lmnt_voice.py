# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
from .lmnt_voice_voice_id import LmntVoiceVoiceId
from .chunk_plan import ChunkPlan
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class LmntVoice(UniversalBaseModel):
    filler_injection_enabled: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="fillerInjectionEnabled")
    ] = pydantic.Field(default=None)
    """
    This determines whether fillers are injected into the model output before inputting it into the voice provider.
    
    Default `false` because you can achieve better results with prompting the model.
    """

    voice_id: typing_extensions.Annotated[LmntVoiceVoiceId, FieldMetadata(alias="voiceId")] = pydantic.Field()
    """
    This is the provider-specific ID that will be used.
    """

    speed: typing.Optional[float] = pydantic.Field(default=None)
    """
    This is the speed multiplier that will be used.
    """

    chunk_plan: typing_extensions.Annotated[typing.Optional[ChunkPlan], FieldMetadata(alias="chunkPlan")] = (
        pydantic.Field(default=None)
    )
    """
    This is the plan for chunking the model output before it is sent to the voice provider.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
