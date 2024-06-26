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
from openapi_client.models.condition import Condition
from openapi_client.models.fulfilment import Fulfilment
from openapi_client.models.pricing import Pricing
from openapi_client.models.stock_create import StockCreate
from typing import Optional, Set
from typing_extensions import Self

class CreateOfferRequest(BaseModel):
    """
    CreateOfferRequest
    """ # noqa: E501
    ean: StrictStr = Field(description="The EAN number associated with this product. Note: in case an ISBN is provided, the ISBN will be replaced with the actual EAN belonging to this ISBN.")
    condition: Condition
    reference: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=20)]] = Field(default=None, description="A user-defined reference that helps you identify this particular offer when receiving data from us. This element can optionally be left empty and has a maximum amount of 20 characters.")
    on_hold_by_retailer: Optional[StrictBool] = Field(default=False, description="This field specifies whether the retailer has temporarily suspended the listing of this offer on the bol.com website. When set to true, the offer becomes invisible to customers and is not available for purchase. The default setting, false, indicates that the offer is active and visible on the website. This feature is useful for managing inventory or making updates to the offer without permanently removing it from the site.", alias="onHoldByRetailer")
    unknown_product_title: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=500)]] = Field(default=None, description="In case the item is not known to bol.com you can use this field to identify this particular product. Note: in case the product is known to bol.com, the unknown product title will not be stored.", alias="unknownProductTitle")
    pricing: Pricing
    stock: StockCreate
    fulfilment: Fulfilment
    __properties: ClassVar[List[str]] = ["ean", "condition", "reference", "onHoldByRetailer", "unknownProductTitle", "pricing", "stock", "fulfilment"]

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
        """Create an instance of CreateOfferRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of condition
        if self.condition:
            _dict['condition'] = self.condition.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pricing
        if self.pricing:
            _dict['pricing'] = self.pricing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of stock
        if self.stock:
            _dict['stock'] = self.stock.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fulfilment
        if self.fulfilment:
            _dict['fulfilment'] = self.fulfilment.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreateOfferRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ean": obj.get("ean"),
            "condition": Condition.from_dict(obj["condition"]) if obj.get("condition") is not None else None,
            "reference": obj.get("reference"),
            "onHoldByRetailer": obj.get("onHoldByRetailer") if obj.get("onHoldByRetailer") is not None else False,
            "unknownProductTitle": obj.get("unknownProductTitle"),
            "pricing": Pricing.from_dict(obj["pricing"]) if obj.get("pricing") is not None else None,
            "stock": StockCreate.from_dict(obj["stock"]) if obj.get("stock") is not None else None,
            "fulfilment": Fulfilment.from_dict(obj["fulfilment"]) if obj.get("fulfilment") is not None else None
        })
        return _obj


