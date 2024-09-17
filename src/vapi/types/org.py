# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing_extensions
import typing
from ..core.serialization import FieldMetadata
import pydantic
import datetime as dt
from .org_plan import OrgPlan
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class Org(UniversalBaseModel):
    hipaa_enabled: typing_extensions.Annotated[typing.Optional[bool], FieldMetadata(alias="hipaaEnabled")] = (
        pydantic.Field(default=None)
    )
    """
    When this is enabled, no logs, recordings, or transcriptions will be stored. At the end of the call, you will still receive an end-of-call-report message to store on your server. Defaults to false.
    When HIPAA is enabled, only OpenAI/Custom LLM or Azure Providers will be available for LLM and Voice respectively.
    This is due to the compliance requirements of HIPAA. Other providers may not meet these requirements.
    """

    id: str = pydantic.Field()
    """
    This is the unique identifier for the org.
    """

    created_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="createdAt")] = pydantic.Field()
    """
    This is the ISO 8601 date-time string of when the org was created.
    """

    updated_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="updatedAt")] = pydantic.Field()
    """
    This is the ISO 8601 date-time string of when the org was last updated.
    """

    stripe_customer_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="stripeCustomerId")] = (
        pydantic.Field(default=None)
    )
    """
    This is the Stripe customer for the org.
    """

    stripe_subscription_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="stripeSubscriptionId")
    ] = pydantic.Field(default=None)
    """
    This is the subscription for the org.
    """

    stripe_subscription_item_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="stripeSubscriptionItemId")
    ] = pydantic.Field(default=None)
    """
    This is the subscription's subscription item.
    """

    stripe_subscription_current_period_start: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="stripeSubscriptionCurrentPeriodStart")
    ] = pydantic.Field(default=None)
    """
    This is the subscription's current period start.
    """

    stripe_subscription_status: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="stripeSubscriptionStatus")
    ] = pydantic.Field(default=None)
    """
    This is the subscription's status.
    """

    plan: typing.Optional[OrgPlan] = pydantic.Field(default=None)
    """
    This is the plan for the org.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    This is the name of the org. This is just for your own reference.
    """

    billing_limit: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="billingLimit")] = (
        pydantic.Field(default=None)
    )
    """
    This is the monthly billing limit for the org. To go beyond $1000/mo, please contact us at support@vapi.ai.
    """

    server_url: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="serverUrl")] = pydantic.Field(
        default=None
    )
    """
    This is the URL Vapi will communicate with via HTTP GET and POST Requests. This is used for retrieving context, function calling, and end-of-call reports.
    
    All requests will be sent with the call object among other things relevant to that message. You can find more details in the Server URL documentation.
    """

    server_url_secret: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="serverUrlSecret")] = (
        pydantic.Field(default=None)
    )
    """
    This is the secret you can set that Vapi will send with every request to your server. Will be sent as a header called x-vapi-secret.
    """

    concurrency_limit: typing_extensions.Annotated[typing.Optional[float], FieldMetadata(alias="concurrencyLimit")] = (
        pydantic.Field(default=None)
    )
    """
    This is the concurrency limit for the org. This is the maximum number of calls that can be active at any given time. To go beyond 10, please contact us at support@vapi.ai.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow