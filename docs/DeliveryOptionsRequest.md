# DeliveryOptionsRequest

The configuration of order items to get delivery options for.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_items** | [**List[DeliveryOptionsRequestOrderItem]**](DeliveryOptionsRequestOrderItem.md) | Order items for which the delivery options are requested. | 

## Example

```python
from openapi_client.models.delivery_options_request import DeliveryOptionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOptionsRequest from a JSON string
delivery_options_request_instance = DeliveryOptionsRequest.from_json(json)
# print the JSON string representation of the object
print(DeliveryOptionsRequest.to_json())

# convert the object into a dict
delivery_options_request_dict = delivery_options_request_instance.to_dict()
# create an instance of DeliveryOptionsRequest from a dict
delivery_options_request_from_dict = DeliveryOptionsRequest.from_dict(delivery_options_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


