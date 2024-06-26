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
from openapi_client.models.upload_report_value import UploadReportValue
from typing import Optional, Set
from typing_extensions import Self

class UploadReportAttribute(BaseModel):
    """
    UploadReportAttribute
    """ # noqa: E501
    id: StrictStr = Field(description="The identifier of the attribute for which the value has changed.")
    values: List[UploadReportValue]
    status: StrictStr = Field(description="The processing state of the submitted attribute.")
    sub_status: Optional[StrictStr] = Field(default=None, description="The reason code explaining why the value was rejected.", alias="subStatus")
    sub_status_description: Optional[StrictStr] = Field(default=None, description="The reason explaining why the value was rejected.", alias="subStatusDescription")
    __properties: ClassVar[List[str]] = ["id", "values", "status", "subStatus", "subStatusDescription"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['IN_PROGRESS', 'DECLINED', 'PUBLISHED']):
            raise ValueError("must be one of enum values ('IN_PROGRESS', 'DECLINED', 'PUBLISHED')")
        return value

    @field_validator('sub_status')
    def sub_status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['BLOCKED_BY_RATE_LIMITER', 'CREATED', 'DEPRECATED', 'IDENTICAL_VALUE_AS_BEFORE', 'MATCH_TO_PRODUCT_FAILED', 'NOT_CHANGED', 'NOT_RECENT', 'PROCESSING_STARTED', 'RECEIVED', 'REJECTED', 'REJECTED_BY_BRAND_AUTHORITY', 'REJECTED_BY_LOGISTIC', 'REJECTED_NO_DATA', 'REJECTED_UNPROCESSABLE', 'SELECTED', 'SELECTED_BY_BRAND_AUTHORITY', 'SELECTED_BY_LOGISTIC', 'SELECTION_DELETED', 'SELECTION_MERGED', 'TIMED_OUT', 'UPDATED', 'UPLOADED', 'UNKNOWN', 'VALID_EAN', 'VALIDATED', 'VALIDATION_FAILED', 'VALIDATION_FAILED_DISABLED_GPC_CODE', 'VALIDATION_FAILED_DOES_NOT_EXIST', 'VALIDATION_FAILED_INVALID_DATE', 'VALIDATION_FAILED_INVALID_EAN', 'VALIDATION_FAILED_INVALID_FRACTION', 'VALIDATION_FAILED_INVALID_GPC_CODE', 'VALIDATION_FAILED_INVALID_INTEGER', 'VALIDATION_FAILED_INVALID_ISODATE', 'VALIDATION_FAILED_INVALID_ISODATETIME', 'VALIDATION_FAILED_INVALID_LOV_VALUE', 'VALIDATION_FAILED_INVALID_MULTIPLE_VALUES', 'VALIDATION_FAILED_INVALID_NO_VALUES', 'VALIDATION_FAILED_INVALID_NUMBER', 'VALIDATION_FAILED_INVALID_NUMERIC_TEXT', 'VALIDATION_FAILED_INVALID_TEXT', 'VALIDATION_FAILED_INVALID_UNIT', 'VALIDATION_FAILED_INVALID_URL', 'VALIDATION_FAILED_INVALID_VALUES', 'VALIDATION_FAILED_NOT_ALLOWED', 'VALIDATION_FAILED_UNKNOWN_BASETYPE', 'WAITING_FOR_GLOBAL_ID']):
            raise ValueError("must be one of enum values ('BLOCKED_BY_RATE_LIMITER', 'CREATED', 'DEPRECATED', 'IDENTICAL_VALUE_AS_BEFORE', 'MATCH_TO_PRODUCT_FAILED', 'NOT_CHANGED', 'NOT_RECENT', 'PROCESSING_STARTED', 'RECEIVED', 'REJECTED', 'REJECTED_BY_BRAND_AUTHORITY', 'REJECTED_BY_LOGISTIC', 'REJECTED_NO_DATA', 'REJECTED_UNPROCESSABLE', 'SELECTED', 'SELECTED_BY_BRAND_AUTHORITY', 'SELECTED_BY_LOGISTIC', 'SELECTION_DELETED', 'SELECTION_MERGED', 'TIMED_OUT', 'UPDATED', 'UPLOADED', 'UNKNOWN', 'VALID_EAN', 'VALIDATED', 'VALIDATION_FAILED', 'VALIDATION_FAILED_DISABLED_GPC_CODE', 'VALIDATION_FAILED_DOES_NOT_EXIST', 'VALIDATION_FAILED_INVALID_DATE', 'VALIDATION_FAILED_INVALID_EAN', 'VALIDATION_FAILED_INVALID_FRACTION', 'VALIDATION_FAILED_INVALID_GPC_CODE', 'VALIDATION_FAILED_INVALID_INTEGER', 'VALIDATION_FAILED_INVALID_ISODATE', 'VALIDATION_FAILED_INVALID_ISODATETIME', 'VALIDATION_FAILED_INVALID_LOV_VALUE', 'VALIDATION_FAILED_INVALID_MULTIPLE_VALUES', 'VALIDATION_FAILED_INVALID_NO_VALUES', 'VALIDATION_FAILED_INVALID_NUMBER', 'VALIDATION_FAILED_INVALID_NUMERIC_TEXT', 'VALIDATION_FAILED_INVALID_TEXT', 'VALIDATION_FAILED_INVALID_UNIT', 'VALIDATION_FAILED_INVALID_URL', 'VALIDATION_FAILED_INVALID_VALUES', 'VALIDATION_FAILED_NOT_ALLOWED', 'VALIDATION_FAILED_UNKNOWN_BASETYPE', 'WAITING_FOR_GLOBAL_ID')")
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
        """Create an instance of UploadReportAttribute from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in values (list)
        _items = []
        if self.values:
            for _item in self.values:
                if _item:
                    _items.append(_item.to_dict())
            _dict['values'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UploadReportAttribute from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "values": [UploadReportValue.from_dict(_item) for _item in obj["values"]] if obj.get("values") is not None else None,
            "status": obj.get("status"),
            "subStatus": obj.get("subStatus"),
            "subStatusDescription": obj.get("subStatusDescription")
        })
        return _obj


