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
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class LoadCarrier(BaseModel):
    """
    LoadCarrier
    """ # noqa: E501
    sscc: Optional[StrictStr] = Field(default=None, description="The Serial Shipping Container Code (SSCC) for this load carrier.")
    transport_label_track_and_trace: Optional[StrictStr] = Field(default=None, description="The track and trace code for this load carrier.", alias="transportLabelTrackAndTrace")
    transport_state: StrictStr = Field(description="The current state of the transport for this load carrier.", alias="transportState")
    transport_state_update_date_time: datetime = Field(description="The date and time in ISO 8601 format when the latest update for this transport was received.", alias="transportStateUpdateDateTime")
    __properties: ClassVar[List[str]] = ["sscc", "transportLabelTrackAndTrace", "transportState", "transportStateUpdateDateTime"]

    @field_validator('transport_state')
    def transport_state_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['ANNOUNCED', 'PICKED_UP', 'UNDERWAY', 'DELAYED', 'ARRIVED', 'ERROR']):
            raise ValueError("must be one of enum values ('ANNOUNCED', 'PICKED_UP', 'UNDERWAY', 'DELAYED', 'ARRIVED', 'ERROR')")
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
        """Create an instance of LoadCarrier from a JSON string"""
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
        """Create an instance of LoadCarrier from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sscc": obj.get("sscc"),
            "transportLabelTrackAndTrace": obj.get("transportLabelTrackAndTrace"),
            "transportState": obj.get("transportState"),
            "transportStateUpdateDateTime": obj.get("transportStateUpdateDateTime")
        })
        return _obj


