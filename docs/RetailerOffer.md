# RetailerOffer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_id** | **str** | Unique identifier for an offer. | 
**ean** | **str** | The EAN number associated with this product. Note: in case an ISBN is provided, the ISBN will be replaced with the actual EAN belonging to this ISBN. | 
**reference** | **str** | A user-defined reference that helps you identify this particular offer when receiving data from us. This element can optionally be left empty and has a maximum amount of 20 characters. | [optional] 
**on_hold_by_retailer** | **bool** | This field specifies whether the retailer has temporarily suspended the listing of this offer on the bol.com website. When set to true, the offer becomes invisible to customers and is not available for purchase. The default setting, false, indicates that the offer is active and visible on the website. This feature is useful for managing inventory or making updates to the offer without permanently removing it from the site. | 
**unknown_product_title** | **str** | In case the item is not known to bol.com you can use this field to identify this particular product. Note: in case the product is known to bol.com, the unknown product title will not be stored. | [optional] 
**pricing** | [**Pricing**](Pricing.md) |  | 
**stock** | [**Stock**](Stock.md) |  | 
**fulfilment** | [**Fulfilment**](Fulfilment.md) |  | 
**store** | [**Store**](Store.md) |  | 
**condition** | [**Condition**](Condition.md) |  | 
**not_publishable_reasons** | [**List[NotPublishableReason]**](NotPublishableReason.md) |  | 

## Example

```python
from openapi_client.models.retailer_offer import RetailerOffer

# TODO update the JSON string below
json = "{}"
# create an instance of RetailerOffer from a JSON string
retailer_offer_instance = RetailerOffer.from_json(json)
# print the JSON string representation of the object
print(RetailerOffer.to_json())

# convert the object into a dict
retailer_offer_dict = retailer_offer_instance.to_dict()
# create an instance of RetailerOffer from a dict
retailer_offer_from_dict = RetailerOffer.from_dict(retailer_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


