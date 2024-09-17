# This file was auto-generated by Fern from our API Definition.

from ..core.pydantic_utilities import UniversalBaseModel
import typing
import pydantic
import typing_extensions
from ..core.serialization import FieldMetadata
import datetime as dt
from ..core.pydantic_utilities import IS_PYDANTIC_V2


class S3Credential(UniversalBaseModel):
    provider: typing.Literal["s3"] = pydantic.Field(default="s3")
    """
    Credential provider. Only allowed value is s3
    """

    aws_access_key_id: typing_extensions.Annotated[str, FieldMetadata(alias="awsAccessKeyId")] = pydantic.Field()
    """
    AWS access key ID.
    """

    aws_secret_access_key: typing_extensions.Annotated[str, FieldMetadata(alias="awsSecretAccessKey")] = (
        pydantic.Field()
    )
    """
    AWS access key secret. This is not returned in the API.
    """

    region: str = pydantic.Field()
    """
    AWS region in which the S3 bucket is located.
    """

    s_3_bucket_name: typing_extensions.Annotated[str, FieldMetadata(alias="s3BucketName")] = pydantic.Field()
    """
    AWS S3 bucket name.
    """

    s_3_path_prefix: typing_extensions.Annotated[str, FieldMetadata(alias="s3PathPrefix")] = pydantic.Field()
    """
    The path prefix for the uploaded recording. Ex. "recordings/"
    """

    id: str = pydantic.Field()
    """
    This is the unique identifier for the credential.
    """

    org_id: typing_extensions.Annotated[str, FieldMetadata(alias="orgId")] = pydantic.Field()
    """
    This is the unique identifier for the org that this credential belongs to.
    """

    created_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="createdAt")] = pydantic.Field()
    """
    This is the ISO 8601 date-time string of when the credential was created.
    """

    updated_at: typing_extensions.Annotated[dt.datetime, FieldMetadata(alias="updatedAt")] = pydantic.Field()
    """
    This is the ISO 8601 date-time string of when the assistant was last updated.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)  # type: ignore # Pydantic v2
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow