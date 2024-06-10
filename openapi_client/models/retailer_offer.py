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
from openapi_client.models.condition import Condition
from openapi_client.models.fulfilment import Fulfilment
from openapi_client.models.not_publishable_reason import NotPublishableReason
from openapi_client.models.pricing import Pricing
from openapi_client.models.stock import Stock
from openapi_client.models.store import Store
from typing import Optional, Set
from typing_extensions import Self

class RetailerOffer(BaseModel):
    """
    RetailerOffer
    """ # noqa: E501
    offer_id: StrictStr = Field(description="Unique identifier for an offer.", alias="offerId")
    ean: StrictStr = Field(description="The EAN number associated with this product. Note: in case an ISBN is provided, the ISBN will be replaced with the actual EAN belonging to this ISBN.")
    reference: Optional[StrictStr] = Field(default=None, description="A user-defined reference that helps you identify this particular offer when receiving data from us. This element can optionally be left empty and has a maximum amount of 20 characters.")
    on_hold_by_retailer: StrictBool = Field(description="This field specifies whether the retailer has temporarily suspended the listing of this offer on the bol.com website. When set to true, the offer becomes invisible to customers and is not available for purchase. The default setting, false, indicates that the offer is active and visible on the website. This feature is useful for managing inventory or making updates to the offer without permanently removing it from the site.", alias="onHoldByRetailer")
    unknown_product_title: Optional[StrictStr] = Field(default=None, description="In case the item is not known to bol.com you can use this field to identify this particular product. Note: in case the product is known to bol.com, the unknown product title will not be stored.", alias="unknownProductTitle")
    pricing: Pricing
    stock: Stock
    fulfilment: Fulfilment
    store: Store
    condition: Condition
    not_publishable_reasons: List[NotPublishableReason] = Field(alias="notPublishableReasons")
    __properties: ClassVar[List[str]] = ["offerId", "ean", "reference", "onHoldByRetailer", "unknownProductTitle", "pricing", "stock", "fulfilment", "store", "condition", "notPublishableReasons"]

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
        """Create an instance of RetailerOffer from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of pricing
        if self.pricing:
            _dict['pricing'] = self.pricing.to_dict()
        # override the default output from pydantic by calling `to_dict()` of stock
        if self.stock:
            _dict['stock'] = self.stock.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fulfilment
        if self.fulfilment:
            _dict['fulfilment'] = self.fulfilment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of store
        if self.store:
            _dict['store'] = self.store.to_dict()
        # override the default output from pydantic by calling `to_dict()` of condition
        if self.condition:
            _dict['condition'] = self.condition.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in not_publishable_reasons (list)
        _items = []
        if self.not_publishable_reasons:
            for _item in self.not_publishable_reasons:
                if _item:
                    _items.append(_item.to_dict())
            _dict['notPublishableReasons'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RetailerOffer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "offerId": obj.get("offerId"),
            "ean": obj.get("ean"),
            "reference": obj.get("reference"),
            "onHoldByRetailer": obj.get("onHoldByRetailer"),
            "unknownProductTitle": obj.get("unknownProductTitle"),
            "pricing": Pricing.from_dict(obj["pricing"]) if obj.get("pricing") is not None else None,
            "stock": Stock.from_dict(obj["stock"]) if obj.get("stock") is not None else None,
            "fulfilment": Fulfilment.from_dict(obj["fulfilment"]) if obj.get("fulfilment") is not None else None,
            "store": Store.from_dict(obj["store"]) if obj.get("store") is not None else None,
            "condition": Condition.from_dict(obj["condition"]) if obj.get("condition") is not None else None,
            "notPublishableReasons": [NotPublishableReason.from_dict(_item) for _item in obj["notPublishableReasons"]] if obj.get("notPublishableReasons") is not None else None
        })
        return _obj


