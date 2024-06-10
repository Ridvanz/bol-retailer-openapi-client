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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ProductDestinationAddress(BaseModel):
    """
    ProductDestinationAddress
    """ # noqa: E501
    street_name: StrictStr = Field(description="The street name of the bol.com warehouse address.", alias="streetName")
    house_number: StrictInt = Field(description="The house number of the bol.com warehouse address.", alias="houseNumber")
    zip_code: StrictStr = Field(description="The zipcode of the bol.com warehouse address.", alias="zipCode")
    city: StrictStr = Field(description="The city of the bol.com warehouse address.")
    country_code: StrictStr = Field(description="The ISO 3166-2 country code of the bol.com warehouse address.", alias="countryCode")
    attention_of: StrictStr = Field(description="Name of the person responsible for this replenishment.", alias="attentionOf")
    house_number_extension: Optional[StrictStr] = Field(default=None, description="The house number extension of the bol.com warehouse address.", alias="houseNumberExtension")
    __properties: ClassVar[List[str]] = ["streetName", "houseNumber", "zipCode", "city", "countryCode", "attentionOf", "houseNumberExtension"]

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
        """Create an instance of ProductDestinationAddress from a JSON string"""
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
        """Create an instance of ProductDestinationAddress from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "streetName": obj.get("streetName"),
            "houseNumber": obj.get("houseNumber"),
            "zipCode": obj.get("zipCode"),
            "city": obj.get("city"),
            "countryCode": obj.get("countryCode"),
            "attentionOf": obj.get("attentionOf"),
            "houseNumberExtension": obj.get("houseNumberExtension")
        })
        return _obj

