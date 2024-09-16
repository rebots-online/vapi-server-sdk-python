# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .block_complete_message_conditions_item import BlockCompleteMessageConditionsItem
import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class BlockCompleteMessage(UniversalBaseModel):
    conditions: typing.Optional[typing.List[BlockCompleteMessageConditionsItem]] = pydantic.Field(default=None)
    """
    This is an optional array of conditions that must be met for this message to be triggered.
    """

    content: str = pydantic.Field()
    """
    This is the content that the assistant will say when this message is triggered.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
