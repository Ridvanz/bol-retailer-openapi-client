# coding: utf-8

"""
    v10 - Retailer API

    The bol.com API for retailers.  # Authentication Our API requires authentication via OAuth2. The detailed steps to authenticate are explained [here](https://api.bol.com/retailer/public/Retailer-API/authentication.html)   # Demo scenarios Our API specification includes examples of the responses you can expect. For more information as well as more examples, we refer you to the following resources:   - [Demo environment](https://api.bol.com/retailer/public/Retailer-API/demo/demo.html) - [Demo scenarios](https://api.bol.com/retailer/public/Retailer-API/demo/v10-index.html) 

    The version of the OpenAPI document: 10.x
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class InvoiceRequestsBillingDetails(BaseModel):
    """
    The details of the customer that is responsible for the financial fulfillment of this shipment.
    """ # noqa: E501
    salutation: StrictStr = Field(description="The salutation of the customer.")
    first_name: Optional[StrictStr] = Field(default=None, description="The first name of the customer.", alias="firstName")
    surname: Optional[StrictStr] = Field(default=None, description="The surname of the customer.")
    street_name: Optional[StrictStr] = Field(default=None, description="The street name.", alias="streetName")
    house_number: Optional[StrictStr] = Field(default=None, description="The house number.", alias="houseNumber")
    house_number_extension: Optional[StrictStr] = Field(default=None, description="The extension on the house number.", alias="houseNumberExtension")
    zip_code: Optional[StrictStr] = Field(default=None, description="The ZIP code in '1234AB' format for NL orders and '0000' format for BE orders.", alias="zipCode")
    city: Optional[StrictStr] = Field(default=None, description="The name of the city.")
    country_code: Optional[StrictStr] = Field(default=None, description="The country code.", alias="countryCode")
    company: Optional[StrictStr] = Field(default=None, description="The company name.")
    vat_number: Optional[StrictStr] = Field(default=None, description="The Value Added Tax (VAT) / BTW number for business sellers situated in the Netherlands.", alias="vatNumber")
    kvk_number: Optional[StrictStr] = Field(default=None, description="The Kamer van Koophandel (KvK) number for organizations situated in the Netherlands or ondernemingsnummer for organizations situated in Belgium.", alias="kvkNumber")
    __properties: ClassVar[List[str]] = ["salutation", "firstName", "surname", "streetName", "houseNumber", "houseNumberExtension", "zipCode", "city", "countryCode", "company", "vatNumber", "kvkNumber"]

    @field_validator('salutation')
    def salutation_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['MALE', 'FEMALE', 'UNKNOWN']):
            raise ValueError("must be one of enum values ('MALE', 'FEMALE', 'UNKNOWN')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of InvoiceRequestsBillingDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InvoiceRequestsBillingDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "salutation": obj.get("salutation"),
            "firstName": obj.get("firstName"),
            "surname": obj.get("surname"),
            "streetName": obj.get("streetName"),
            "houseNumber": obj.get("houseNumber"),
            "houseNumberExtension": obj.get("houseNumberExtension"),
            "zipCode": obj.get("zipCode"),
            "city": obj.get("city"),
            "countryCode": obj.get("countryCode"),
            "company": obj.get("company"),
            "vatNumber": obj.get("vatNumber"),
            "kvkNumber": obj.get("kvkNumber")
        })
        return _obj


