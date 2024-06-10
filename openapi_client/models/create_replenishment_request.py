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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.create_delivery_info import CreateDeliveryInfo
from openapi_client.models.create_pickup_appointment import CreatePickupAppointment
from openapi_client.models.create_replenishment_line import CreateReplenishmentLine
from typing import Optional, Set
from typing_extensions import Self

class CreateReplenishmentRequest(BaseModel):
    """
    CreateReplenishmentRequest
    """ # noqa: E501
    reference: StrictStr = Field(description="Custom user reference for this replenishment. Must contain at least 1 digit and only upper case characters allowed.")
    delivery_info: Optional[CreateDeliveryInfo] = Field(default=None, alias="deliveryInfo")
    labeling_by_bol: StrictBool = Field(description="Indicates whether the replenishment will be labeled by bol.com.", alias="labelingByBol")
    number_of_load_carriers: Annotated[int, Field(le=66, strict=True, ge=1)] = Field(description="The number of parcels in this replenishment. Note: if you are using the bol.com pickup service, the maximum number is 20.", alias="numberOfLoadCarriers")
    pickup_appointment: Optional[CreatePickupAppointment] = Field(default=None, alias="pickupAppointment")
    lines: Annotated[List[CreateReplenishmentLine], Field(min_length=1, max_length=9999)]
    __properties: ClassVar[List[str]] = ["reference", "deliveryInfo", "labelingByBol", "numberOfLoadCarriers", "pickupAppointment", "lines"]

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
        """Create an instance of CreateReplenishmentRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of delivery_info
        if self.delivery_info:
            _dict['deliveryInfo'] = self.delivery_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pickup_appointment
        if self.pickup_appointment:
            _dict['pickupAppointment'] = self.pickup_appointment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in lines (list)
        _items = []
        if self.lines:
            for _item in self.lines:
                if _item:
                    _items.append(_item.to_dict())
            _dict['lines'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateReplenishmentRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "reference": obj.get("reference"),
            "deliveryInfo": CreateDeliveryInfo.from_dict(obj["deliveryInfo"]) if obj.get("deliveryInfo") is not None else None,
            "labelingByBol": obj.get("labelingByBol"),
            "numberOfLoadCarriers": obj.get("numberOfLoadCarriers"),
            "pickupAppointment": CreatePickupAppointment.from_dict(obj["pickupAppointment"]) if obj.get("pickupAppointment") is not None else None,
            "lines": [CreateReplenishmentLine.from_dict(_item) for _item in obj["lines"]] if obj.get("lines") is not None else None
        })
        return _obj

