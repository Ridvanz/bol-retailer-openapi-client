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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.retailer_rating import RetailerRating
from openapi_client.models.retailer_review import RetailerReview
from typing import Optional, Set
from typing_extensions import Self

class RetailerInformationResponse(BaseModel):
    """
    RetailerInformationResponse
    """ # noqa: E501
    retailer_id: StrictStr = Field(description="The Id of the retailer which information belongs to.", alias="retailerId")
    display_name: StrictStr = Field(description="The name of the retailer visible on bol.com", alias="displayName")
    company_name: StrictStr = Field(description="The company name of the retailer.", alias="companyName")
    vat_number: StrictStr = Field(description="The VAT number of the retailer.", alias="vatNumber")
    kvk_number: StrictStr = Field(description="The KVK number of the retailer.", alias="kvkNumber")
    registration_date: StrictStr = Field(description="A date representing the registration date for the retailer within bol.com", alias="registrationDate")
    top_retailer: Optional[StrictBool] = Field(default=None, description="Indication of retailer's being the top seller.", alias="topRetailer")
    rating_method: Optional[StrictStr] = Field(default=None, description="An identifier that identifies if the rating is calculated over the past three months or on all reviews for the retailer.", alias="ratingMethod")
    retailer_rating: Optional[RetailerRating] = Field(default=None, alias="retailerRating")
    retailer_review: Optional[RetailerReview] = Field(default=None, alias="retailerReview")
    __properties: ClassVar[List[str]] = ["retailerId", "displayName", "companyName", "vatNumber", "kvkNumber", "registrationDate", "topRetailer", "ratingMethod", "retailerRating", "retailerReview"]

    @field_validator('rating_method')
    def rating_method_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ALL_REVIEWS', 'THREE_MONTHS']):
            raise ValueError("must be one of enum values ('ALL_REVIEWS', 'THREE_MONTHS')")
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
        """Create an instance of RetailerInformationResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of retailer_rating
        if self.retailer_rating:
            _dict['retailerRating'] = self.retailer_rating.to_dict()
        # override the default output from pydantic by calling `to_dict()` of retailer_review
        if self.retailer_review:
            _dict['retailerReview'] = self.retailer_review.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RetailerInformationResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "retailerId": obj.get("retailerId"),
            "displayName": obj.get("displayName"),
            "companyName": obj.get("companyName"),
            "vatNumber": obj.get("vatNumber"),
            "kvkNumber": obj.get("kvkNumber"),
            "registrationDate": obj.get("registrationDate"),
            "topRetailer": obj.get("topRetailer"),
            "ratingMethod": obj.get("ratingMethod"),
            "retailerRating": RetailerRating.from_dict(obj["retailerRating"]) if obj.get("retailerRating") is not None else None,
            "retailerReview": RetailerReview.from_dict(obj["retailerReview"]) if obj.get("retailerReview") is not None else None
        })
        return _obj

