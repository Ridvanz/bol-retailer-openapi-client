# CreateOfferRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ean** | **str** | The EAN number associated with this product. Note: in case an ISBN is provided, the ISBN will be replaced with the actual EAN belonging to this ISBN. | 
**condition** | [**Condition**](Condition.md) |  | 
**reference** | **str** | A user-defined reference that helps you identify this particular offer when receiving data from us. This element can optionally be left empty and has a maximum amount of 20 characters. | [optional] 
**on_hold_by_retailer** | **bool** | This field specifies whether the retailer has temporarily suspended the listing of this offer on the bol.com website. When set to true, the offer becomes invisible to customers and is not available for purchase. The default setting, false, indicates that the offer is active and visible on the website. This feature is useful for managing inventory or making updates to the offer without permanently removing it from the site. | [optional] [default to False]
**unknown_product_title** | **str** | In case the item is not known to bol.com you can use this field to identify this particular product. Note: in case the product is known to bol.com, the unknown product title will not be stored. | [optional] 
**pricing** | [**Pricing**](Pricing.md) |  | 
**stock** | [**StockCreate**](StockCreate.md) |  | 
**fulfilment** | [**Fulfilment**](Fulfilment.md) |  | 

## Example

```python
from openapi_client.models.create_offer_request import CreateOfferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOfferRequest from a JSON string
create_offer_request_instance = CreateOfferRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOfferRequest.to_json())

# convert the object into a dict
create_offer_request_dict = create_offer_request_instance.to_dict()
# create an instance of CreateOfferRequest from a dict
create_offer_request_from_dict = CreateOfferRequest.from_dict(create_offer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


