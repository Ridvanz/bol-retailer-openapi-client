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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from openapi_client.models.relevance_score import RelevanceScore
from typing import Optional, Set
from typing_extensions import Self

class Product(BaseModel):
    """
    A single product.
    """ # noqa: E501
    ean: StrictStr = Field(description="The EAN number associated with this product.")
    relevance_scores: Optional[List[RelevanceScore]] = Field(default=None, alias="relevanceScores")
    maximum_price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The maximum price a product can have in order to be part of the promotion.", alias="maximumPrice")
    __properties: ClassVar[List[str]] = ["ean", "relevanceScores", "maximumPrice"]

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
        """Create an instance of Product from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in relevance_scores (list)
        _items = []
        if self.relevance_scores:
            for _item in self.relevance_scores:
                if _item:
                    _items.append(_item.to_dict())
            _dict['relevanceScores'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Product from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ean": obj.get("ean"),
            "relevanceScores": [RelevanceScore.from_dict(_item) for _item in obj["relevanceScores"]] if obj.get("relevanceScores") is not None else None,
            "maximumPrice": obj.get("maximumPrice")
        })
        return _obj

