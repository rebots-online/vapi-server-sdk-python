# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import typing_extensions
from ..core.serialization import FieldMetadata
from .format_plan_replacements_item import FormatPlanReplacementsItem
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class FormatPlan(UniversalBaseModel):
    enabled: typing.Optional[bool] = pydantic.Field(default=None)
    """
    This determines whether the chunk is formatted before being sent to the voice provider. This helps with enunciation. This includes phone numbers, emails and addresses. Default `true`.
    
    Usage:
    
    - To rely on the voice provider's formatting logic, set this to `false`.
    - To use ElevenLabs's `enableSsmlParsing` feature, set this to `false`.
    
    If `voice.chunkPlan.enabled` is `false`, this is automatically `false` since there's no chunk to format.
    
    @default true
    """

    number_to_digits_cutoff: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="numberToDigitsCutoff")
    ] = pydantic.Field(default=None)
    """
    This is the cutoff after which a number is converted to individual digits instead of being spoken as words.
    
    Example:
    
    - If cutoff 2025, "12345" is converted to "1 2 3 4 5" while "1200" is converted to "twelve hundred".
    
    Usage:
    
    - If your use case doesn't involve IDs like zip codes, set this to a high value.
    - If your use case involves IDs that are shorter than 5 digits, set this to a lower value.
    
    @default 2025
    """

    replacements: typing.Optional[typing.List[FormatPlanReplacementsItem]] = pydantic.Field(default=None)
    """
    These are the custom replacements you can make to the chunk before it is sent to the voice provider.
    
    Usage:
    
    - To replace a specific word or phrase with a different word or phrase, use the `ExactReplacement` type. Eg. `{ type: 'exact', key: 'hello', value: 'hi' }`
    - To replace a word or phrase that matches a pattern, use the `RegexReplacement` type. Eg. `{ type: 'regex', regex: '\\b[a-zA-Z]{5}\\b', value: 'hi' }`
    
    @default []
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
