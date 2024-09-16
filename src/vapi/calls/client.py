# This file was auto-generated by Fern from our API Definition.

import typing
from ..core.client_wrapper import SyncClientWrapper
import datetime as dt
from ..core.request_options import RequestOptions
from ..types.call import Call
from ..core.datetime_utils import serialize_datetime
from ..core.pydantic_utilities import parse_obj_as
from json.decoder import JSONDecodeError
from ..core.api_error import ApiError
from ..types.create_assistant_dto import CreateAssistantDto
from ..types.assistant_overrides import AssistantOverrides
from ..types.create_squad_dto import CreateSquadDto
from ..types.import_twilio_phone_number_dto import ImportTwilioPhoneNumberDto
from ..types.create_customer_dto import CreateCustomerDto
from ..core.serialization import convert_and_respect_annotation_metadata
from ..core.jsonable_encoder import jsonable_encoder
from ..core.client_wrapper import AsyncClientWrapper

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class CallsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(
        self,
        *,
        assistant_id: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        created_at_gt: typing.Optional[dt.datetime] = None,
        created_at_lt: typing.Optional[dt.datetime] = None,
        created_at_ge: typing.Optional[dt.datetime] = None,
        created_at_le: typing.Optional[dt.datetime] = None,
        updated_at_gt: typing.Optional[dt.datetime] = None,
        updated_at_lt: typing.Optional[dt.datetime] = None,
        updated_at_ge: typing.Optional[dt.datetime] = None,
        updated_at_le: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Call]:
        """
        Parameters
        ----------
        assistant_id : typing.Optional[str]
            This will return calls with the specified assistantId.

        limit : typing.Optional[float]
            This is the maximum number of items to return. Defaults to 100.

        created_at_gt : typing.Optional[dt.datetime]
            This will return items where the createdAt is greater than the specified value.

        created_at_lt : typing.Optional[dt.datetime]
            This will return items where the createdAt is less than the specified value.

        created_at_ge : typing.Optional[dt.datetime]
            This will return items where the createdAt is greater than or equal to the specified value.

        created_at_le : typing.Optional[dt.datetime]
            This will return items where the createdAt is less than or equal to the specified value.

        updated_at_gt : typing.Optional[dt.datetime]
            This will return items where the updatedAt is greater than the specified value.

        updated_at_lt : typing.Optional[dt.datetime]
            This will return items where the updatedAt is less than the specified value.

        updated_at_ge : typing.Optional[dt.datetime]
            This will return items where the updatedAt is greater than or equal to the specified value.

        updated_at_le : typing.Optional[dt.datetime]
            This will return items where the updatedAt is less than or equal to the specified value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Call]


        Examples
        --------
        from vapi import Vapi

        client = Vapi(
            token="YOUR_TOKEN",
        )
        client.calls.list()
        """
        _response = self._client_wrapper.httpx_client.request(
            "call",
            method="GET",
            params={
                "assistantId": assistant_id,
                "limit": limit,
                "createdAtGt": serialize_datetime(created_at_gt) if created_at_gt is not None else None,
                "createdAtLt": serialize_datetime(created_at_lt) if created_at_lt is not None else None,
                "createdAtGe": serialize_datetime(created_at_ge) if created_at_ge is not None else None,
                "createdAtLe": serialize_datetime(created_at_le) if created_at_le is not None else None,
                "updatedAtGt": serialize_datetime(updated_at_gt) if updated_at_gt is not None else None,
                "updatedAtLt": serialize_datetime(updated_at_lt) if updated_at_lt is not None else None,
                "updatedAtGe": serialize_datetime(updated_at_ge) if updated_at_ge is not None else None,
                "updatedAtLe": serialize_datetime(updated_at_le) if updated_at_le is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[Call],
                    parse_obj_as(
                        type_=typing.List[Call],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create(
        self,
        *,
        name: typing.Optional[str] = OMIT,
        assistant_id: typing.Optional[str] = OMIT,
        assistant: typing.Optional[CreateAssistantDto] = OMIT,
        assistant_overrides: typing.Optional[AssistantOverrides] = OMIT,
        squad_id: typing.Optional[str] = OMIT,
        squad: typing.Optional[CreateSquadDto] = OMIT,
        phone_number_id: typing.Optional[str] = OMIT,
        phone_number: typing.Optional[ImportTwilioPhoneNumberDto] = OMIT,
        customer_id: typing.Optional[str] = OMIT,
        customer: typing.Optional[CreateCustomerDto] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Call:
        """
        Parameters
        ----------
        name : typing.Optional[str]
            This is the name of the call. This is just for your own reference.

        assistant_id : typing.Optional[str]
            This is the assistant that will be used for the call. To use a transient assistant, use `assistant` instead.

        assistant : typing.Optional[CreateAssistantDto]
            This is the assistant that will be used for the call. To use an existing assistant, use `assistantId` instead.

        assistant_overrides : typing.Optional[AssistantOverrides]
            These are the overrides for the `assistant` or `assistantId`'s settings and template variables.

        squad_id : typing.Optional[str]
            This is the squad that will be used for the call. To use a transient squad, use `squad` instead.

        squad : typing.Optional[CreateSquadDto]
            This is a squad that will be used for the call. To use an existing squad, use `squadId` instead.

        phone_number_id : typing.Optional[str]
            This is the phone number that will be used for the call. To use a transient number, use `phoneNumber` instead.

            Only relevant for `outboundPhoneCall` and `inboundPhoneCall` type.

        phone_number : typing.Optional[ImportTwilioPhoneNumberDto]
            This is the phone number that will be used for the call. To use an existing number, use `phoneNumberId` instead.

            Only relevant for `outboundPhoneCall` and `inboundPhoneCall` type.

        customer_id : typing.Optional[str]
            This is the customer that will be called. To call a transient customer , use `customer` instead.

            Only relevant for `outboundPhoneCall` and `inboundPhoneCall` type.

        customer : typing.Optional[CreateCustomerDto]
            This is the customer that will be called. To call an existing customer, use `customerId` instead.

            Only relevant for `outboundPhoneCall` and `inboundPhoneCall` type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Call


        Examples
        --------
        from vapi import Vapi

        client = Vapi(
            token="YOUR_TOKEN",
        )
        client.calls.create()
        """
        _response = self._client_wrapper.httpx_client.request(
            "call",
            method="POST",
            json={
                "name": name,
                "assistantId": assistant_id,
                "assistant": convert_and_respect_annotation_metadata(
                    object_=assistant, annotation=CreateAssistantDto, direction="write"
                ),
                "assistantOverrides": convert_and_respect_annotation_metadata(
                    object_=assistant_overrides, annotation=AssistantOverrides, direction="write"
                ),
                "squadId": squad_id,
                "squad": convert_and_respect_annotation_metadata(
                    object_=squad, annotation=CreateSquadDto, direction="write"
                ),
                "phoneNumberId": phone_number_id,
                "phoneNumber": convert_and_respect_annotation_metadata(
                    object_=phone_number, annotation=ImportTwilioPhoneNumberDto, direction="write"
                ),
                "customerId": customer_id,
                "customer": convert_and_respect_annotation_metadata(
                    object_=customer, annotation=CreateCustomerDto, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Call,
                    parse_obj_as(
                        type_=Call,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Call:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Call


        Examples
        --------
        from vapi import Vapi

        client = Vapi(
            token="YOUR_TOKEN",
        )
        client.calls.get(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"call/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Call,
                    parse_obj_as(
                        type_=Call,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Call:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Call


        Examples
        --------
        from vapi import Vapi

        client = Vapi(
            token="YOUR_TOKEN",
        )
        client.calls.delete(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"call/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Call,
                    parse_obj_as(
                        type_=Call,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self, id: str, *, name: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> Call:
        """
        Parameters
        ----------
        id : str

        name : typing.Optional[str]
            This is the name of the call. This is just for your own reference.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Call


        Examples
        --------
        from vapi import Vapi

        client = Vapi(
            token="YOUR_TOKEN",
        )
        client.calls.update(
            id="id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            f"call/{jsonable_encoder(id)}",
            method="PATCH",
            json={
                "name": name,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Call,
                    parse_obj_as(
                        type_=Call,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncCallsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(
        self,
        *,
        assistant_id: typing.Optional[str] = None,
        limit: typing.Optional[float] = None,
        created_at_gt: typing.Optional[dt.datetime] = None,
        created_at_lt: typing.Optional[dt.datetime] = None,
        created_at_ge: typing.Optional[dt.datetime] = None,
        created_at_le: typing.Optional[dt.datetime] = None,
        updated_at_gt: typing.Optional[dt.datetime] = None,
        updated_at_lt: typing.Optional[dt.datetime] = None,
        updated_at_ge: typing.Optional[dt.datetime] = None,
        updated_at_le: typing.Optional[dt.datetime] = None,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> typing.List[Call]:
        """
        Parameters
        ----------
        assistant_id : typing.Optional[str]
            This will return calls with the specified assistantId.

        limit : typing.Optional[float]
            This is the maximum number of items to return. Defaults to 100.

        created_at_gt : typing.Optional[dt.datetime]
            This will return items where the createdAt is greater than the specified value.

        created_at_lt : typing.Optional[dt.datetime]
            This will return items where the createdAt is less than the specified value.

        created_at_ge : typing.Optional[dt.datetime]
            This will return items where the createdAt is greater than or equal to the specified value.

        created_at_le : typing.Optional[dt.datetime]
            This will return items where the createdAt is less than or equal to the specified value.

        updated_at_gt : typing.Optional[dt.datetime]
            This will return items where the updatedAt is greater than the specified value.

        updated_at_lt : typing.Optional[dt.datetime]
            This will return items where the updatedAt is less than the specified value.

        updated_at_ge : typing.Optional[dt.datetime]
            This will return items where the updatedAt is greater than or equal to the specified value.

        updated_at_le : typing.Optional[dt.datetime]
            This will return items where the updatedAt is less than or equal to the specified value.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Call]


        Examples
        --------
        import asyncio

        from vapi import AsyncVapi

        client = AsyncVapi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.calls.list()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "call",
            method="GET",
            params={
                "assistantId": assistant_id,
                "limit": limit,
                "createdAtGt": serialize_datetime(created_at_gt) if created_at_gt is not None else None,
                "createdAtLt": serialize_datetime(created_at_lt) if created_at_lt is not None else None,
                "createdAtGe": serialize_datetime(created_at_ge) if created_at_ge is not None else None,
                "createdAtLe": serialize_datetime(created_at_le) if created_at_le is not None else None,
                "updatedAtGt": serialize_datetime(updated_at_gt) if updated_at_gt is not None else None,
                "updatedAtLt": serialize_datetime(updated_at_lt) if updated_at_lt is not None else None,
                "updatedAtGe": serialize_datetime(updated_at_ge) if updated_at_ge is not None else None,
                "updatedAtLe": serialize_datetime(updated_at_le) if updated_at_le is not None else None,
            },
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    typing.List[Call],
                    parse_obj_as(
                        type_=typing.List[Call],  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create(
        self,
        *,
        name: typing.Optional[str] = OMIT,
        assistant_id: typing.Optional[str] = OMIT,
        assistant: typing.Optional[CreateAssistantDto] = OMIT,
        assistant_overrides: typing.Optional[AssistantOverrides] = OMIT,
        squad_id: typing.Optional[str] = OMIT,
        squad: typing.Optional[CreateSquadDto] = OMIT,
        phone_number_id: typing.Optional[str] = OMIT,
        phone_number: typing.Optional[ImportTwilioPhoneNumberDto] = OMIT,
        customer_id: typing.Optional[str] = OMIT,
        customer: typing.Optional[CreateCustomerDto] = OMIT,
        request_options: typing.Optional[RequestOptions] = None,
    ) -> Call:
        """
        Parameters
        ----------
        name : typing.Optional[str]
            This is the name of the call. This is just for your own reference.

        assistant_id : typing.Optional[str]
            This is the assistant that will be used for the call. To use a transient assistant, use `assistant` instead.

        assistant : typing.Optional[CreateAssistantDto]
            This is the assistant that will be used for the call. To use an existing assistant, use `assistantId` instead.

        assistant_overrides : typing.Optional[AssistantOverrides]
            These are the overrides for the `assistant` or `assistantId`'s settings and template variables.

        squad_id : typing.Optional[str]
            This is the squad that will be used for the call. To use a transient squad, use `squad` instead.

        squad : typing.Optional[CreateSquadDto]
            This is a squad that will be used for the call. To use an existing squad, use `squadId` instead.

        phone_number_id : typing.Optional[str]
            This is the phone number that will be used for the call. To use a transient number, use `phoneNumber` instead.

            Only relevant for `outboundPhoneCall` and `inboundPhoneCall` type.

        phone_number : typing.Optional[ImportTwilioPhoneNumberDto]
            This is the phone number that will be used for the call. To use an existing number, use `phoneNumberId` instead.

            Only relevant for `outboundPhoneCall` and `inboundPhoneCall` type.

        customer_id : typing.Optional[str]
            This is the customer that will be called. To call a transient customer , use `customer` instead.

            Only relevant for `outboundPhoneCall` and `inboundPhoneCall` type.

        customer : typing.Optional[CreateCustomerDto]
            This is the customer that will be called. To call an existing customer, use `customerId` instead.

            Only relevant for `outboundPhoneCall` and `inboundPhoneCall` type.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Call


        Examples
        --------
        import asyncio

        from vapi import AsyncVapi

        client = AsyncVapi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.calls.create()


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            "call",
            method="POST",
            json={
                "name": name,
                "assistantId": assistant_id,
                "assistant": convert_and_respect_annotation_metadata(
                    object_=assistant, annotation=CreateAssistantDto, direction="write"
                ),
                "assistantOverrides": convert_and_respect_annotation_metadata(
                    object_=assistant_overrides, annotation=AssistantOverrides, direction="write"
                ),
                "squadId": squad_id,
                "squad": convert_and_respect_annotation_metadata(
                    object_=squad, annotation=CreateSquadDto, direction="write"
                ),
                "phoneNumberId": phone_number_id,
                "phoneNumber": convert_and_respect_annotation_metadata(
                    object_=phone_number, annotation=ImportTwilioPhoneNumberDto, direction="write"
                ),
                "customerId": customer_id,
                "customer": convert_and_respect_annotation_metadata(
                    object_=customer, annotation=CreateCustomerDto, direction="write"
                ),
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Call,
                    parse_obj_as(
                        type_=Call,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Call:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Call


        Examples
        --------
        import asyncio

        from vapi import AsyncVapi

        client = AsyncVapi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.calls.get(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"call/{jsonable_encoder(id)}",
            method="GET",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Call,
                    parse_obj_as(
                        type_=Call,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete(self, id: str, *, request_options: typing.Optional[RequestOptions] = None) -> Call:
        """
        Parameters
        ----------
        id : str

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Call


        Examples
        --------
        import asyncio

        from vapi import AsyncVapi

        client = AsyncVapi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.calls.delete(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"call/{jsonable_encoder(id)}",
            method="DELETE",
            request_options=request_options,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Call,
                    parse_obj_as(
                        type_=Call,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self, id: str, *, name: typing.Optional[str] = OMIT, request_options: typing.Optional[RequestOptions] = None
    ) -> Call:
        """
        Parameters
        ----------
        id : str

        name : typing.Optional[str]
            This is the name of the call. This is just for your own reference.

        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        Call


        Examples
        --------
        import asyncio

        from vapi import AsyncVapi

        client = AsyncVapi(
            token="YOUR_TOKEN",
        )


        async def main() -> None:
            await client.calls.update(
                id="id",
            )


        asyncio.run(main())
        """
        _response = await self._client_wrapper.httpx_client.request(
            f"call/{jsonable_encoder(id)}",
            method="PATCH",
            json={
                "name": name,
            },
            request_options=request_options,
            omit=OMIT,
        )
        try:
            if 200 <= _response.status_code < 300:
                return typing.cast(
                    Call,
                    parse_obj_as(
                        type_=Call,  # type: ignore
                        object_=_response.json(),
                    ),
                )
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
