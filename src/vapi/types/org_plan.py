# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import pydantic


class OrgPlan(UniversalBaseModel):
    included_providers: typing_extensions.Annotated[
        typing.Optional[typing.List[typing.Dict[str, typing.Optional[typing.Any]]]],
        FieldMetadata(alias="includedProviders"),
    ] = None
    included_minutes: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="includedMinutes")] = None
    cost_per_overage_minute: typing_extensions.Annotated[
        typing.Optional[float], FieldMetadata(alias="costPerOverageMinute")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
