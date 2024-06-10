# OrderOffer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_id** | **str** | Unique identifier for an offer. | [optional] 
**reference** | **str** | A user-defined reference tied to the offer upon creating the offer. | [optional] 

## Example

```python
from openapi_client.models.order_offer import OrderOffer

# TODO update the JSON string below
json = "{}"
# create an instance of OrderOffer from a JSON string
order_offer_instance = OrderOffer.from_json(json)
# print the JSON string representation of the object
print(OrderOffer.to_json())

# convert the object into a dict
order_offer_dict = order_offer_instance.to_dict()
# create an instance of OrderOffer from a dict
order_offer_from_dict = OrderOffer.from_dict(order_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


