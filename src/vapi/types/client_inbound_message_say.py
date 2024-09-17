# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import typing_extensions
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class ClientInboundMessageSay(UniversalBaseModel):
    content: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the content to say.
    """

    end_call_after_spoken: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="endCallAfterSpoken")
    ] = pydantic.Field(default=None)
    """
    This is the flag to end call after content is spoken.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow