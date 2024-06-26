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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from openapi_client.models.reduced_invalid_replenishment_line import ReducedInvalidReplenishmentLine
from openapi_client.models.reduced_replenishment_lines import ReducedReplenishmentLines
from typing import Optional, Set
from typing_extensions import Self

class ReducedReplenishment(BaseModel):
    """
    ReducedReplenishment
    """ # noqa: E501
    replenishment_id: StrictStr = Field(description="The unique identifier of the replenishment.", alias="replenishmentId")
    reference: StrictStr = Field(description="Custom user defined reference to identify the replenishment.")
    creation_date_time: datetime = Field(description="The date and time when this replenishment was created. In ISO 8601 format.", alias="creationDateTime")
    lines: List[ReducedReplenishmentLines]
    invalid_lines: List[ReducedInvalidReplenishmentLine] = Field(alias="invalidLines")
    __properties: ClassVar[List[str]] = ["replenishmentId", "reference", "creationDateTime", "lines", "invalidLines"]

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
        """Create an instance of ReducedReplenishment from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in lines (list)
        _items = []
        if self.lines:
            for _item in self.lines:
                if _item:
                    _items.append(_item.to_dict())
            _dict['lines'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in invalid_lines (list)
        _items = []
        if self.invalid_lines:
            for _item in self.invalid_lines:
                if _item:
                    _items.append(_item.to_dict())
            _dict['invalidLines'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ReducedReplenishment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "replenishmentId": obj.get("replenishmentId"),
            "reference": obj.get("reference"),
            "creationDateTime": obj.get("creationDateTime"),
            "lines": [ReducedReplenishmentLines.from_dict(_item) for _item in obj["lines"]] if obj.get("lines") is not None else None,
            "invalidLines": [ReducedInvalidReplenishmentLine.from_dict(_item) for _item in obj["invalidLines"]] if obj.get("invalidLines") is not None else None
        })
        return _obj


