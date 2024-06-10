# UpdateOfferRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | A user-defined reference that helps you identify this particular offer when receiving data from us. This element can optionally be left empty and has a maximum amount of 20 characters. | [optional] 
**on_hold_by_retailer** | **bool** | This field specifies whether the retailer has temporarily suspended the listing of this offer on the bol.com website. When set to true, the offer becomes invisible to customers and is not available for purchase. The default setting, false, indicates that the offer is active and visible on the website. This feature is useful for managing inventory or making updates to the offer without permanently removing it from the site. | [optional] [default to False]
**unknown_product_title** | **str** | In case the item is not known to bol.com you can use this field to identify this particular product. Note: in case the product is known to bol.com, the unknown product title will not be stored. | [optional] 
**fulfilment** | [**Fulfilment**](Fulfilment.md) |  | 

## Example

```python
from openapi_client.models.update_offer_request import UpdateOfferRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOfferRequest from a JSON string
update_offer_request_instance = UpdateOfferRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateOfferRequest.to_json())

# convert the object into a dict
update_offer_request_dict = update_offer_request_instance.to_dict()
# create an instance of UpdateOfferRequest from a dict
update_offer_request_from_dict = UpdateOfferRequest.from_dict(update_offer_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


