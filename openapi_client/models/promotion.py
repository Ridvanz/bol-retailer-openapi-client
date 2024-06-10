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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.campaign import Campaign
from openapi_client.models.promotion_country_code import PromotionCountryCode
from typing import Optional, Set
from typing_extensions import Self

class Promotion(BaseModel):
    """
    A single promotion.
    """ # noqa: E501
    promotion_id: StrictStr = Field(description="The identifier of the promotion.", alias="promotionId")
    title: StrictStr = Field(description="The title of the promotion.")
    start_date_time: datetime = Field(description="The starting date and time of the promotion.", alias="startDateTime")
    end_date_time: datetime = Field(description="The ending date and time of the promotion.", alias="endDateTime")
    countries: List[PromotionCountryCode]
    promotion_type: StrictStr = Field(description="The type of the promotion.", alias="promotionType")
    retailer_specific_promotion: StrictBool = Field(description="Indicates whether the promotion is retailer specific or open to the platform.", alias="retailerSpecificPromotion")
    campaign: Optional[Campaign] = None
    __properties: ClassVar[List[str]] = ["promotionId", "title", "startDateTime", "endDateTime", "countries", "promotionType", "retailerSpecificPromotion", "campaign"]

    @field_validator('promotion_type')
    def promotion_type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['AWARENESS', 'PRICE_OFF']):
            raise ValueError("must be one of enum values ('AWARENESS', 'PRICE_OFF')")
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
        """Create an instance of Promotion from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in countries (list)
        _items = []
        if self.countries:
            for _item in self.countries:
                if _item:
                    _items.append(_item.to_dict())
            _dict['countries'] = _items
        # override the default output from pydantic by calling `to_dict()` of campaign
        if self.campaign:
            _dict['campaign'] = self.campaign.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Promotion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "promotionId": obj.get("promotionId"),
            "title": obj.get("title"),
            "startDateTime": obj.get("startDateTime"),
            "endDateTime": obj.get("endDateTime"),
            "countries": [PromotionCountryCode.from_dict(_item) for _item in obj["countries"]] if obj.get("countries") is not None else None,
            "promotionType": obj.get("promotionType"),
            "retailerSpecificPromotion": obj.get("retailerSpecificPromotion"),
            "campaign": Campaign.from_dict(obj["campaign"]) if obj.get("campaign") is not None else None
        })
        return _obj

