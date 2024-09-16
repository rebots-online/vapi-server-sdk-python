# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import pydantic
from .condition_operator import ConditionOperator
from ..core.pydantic_utilities import IS_PYDANTIC_V2
import typing


class Condition(UniversalBaseModel):
    value: str = pydantic.Field()
    """
    This is the value you want to compare against the parameter.
    """

    operator: ConditionOperator = pydantic.Field()
    """
    This is the operator you want to use to compare the parameter and value.
    """

    param: str = pydantic.Field()
    """
    This is the name of the parameter that you want to check.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
