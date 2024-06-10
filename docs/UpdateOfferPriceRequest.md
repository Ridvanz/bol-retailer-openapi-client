# UpdateOfferPriceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pricing** | [**Pricing**](Pricing.md) |  | 

## Example

```python
from openapi_client.models.update_offer_price_request import UpdateOfferPriceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOfferPriceRequest from a JSON string
update_offer_price_request_instance = UpdateOfferPriceRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateOfferPriceRequest.to_json())

# convert the object into a dict
update_offer_price_request_dict = update_offer_price_request_instance.to_dict()
# create an instance of UpdateOfferPriceRequest from a dict
update_offer_price_request_from_dict = UpdateOfferPriceRequest.from_dict(update_offer_price_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


