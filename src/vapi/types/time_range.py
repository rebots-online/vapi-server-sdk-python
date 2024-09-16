# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
from .time_range_step import TimeRangeStep
import pydantic
import datetime as dt
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class TimeRange(UniversalBaseModel):
    step: typing.Optional[TimeRangeStep] = pydantic.Field(default=None)
    """
    This is the time step for aggregations.
    
    If not provided, defaults to returning for the entire time range.
    """

    start: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    This is the start date for the time range.
    
    If not provided, defaults to the 7 days ago.
    """

    end: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    This is the end date for the time range.
    
    If not provided, defaults to now.
    """

    timezone: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the timezone you want to set for the query.
    
    If not provided, defaults to UTC.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
