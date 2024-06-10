# DeliveryOptionsRequestOrderItem

Order items for which the delivery options are requested.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_item_id** | **str** | The id for the order item (1 order can have multiple order items). | 
**quantity** | **int** | The quantity of the order item for which the shipping label creation is requested for. If omitted, will be interpreted as the full quantity that is still open for this order item. | [optional] 

## Example

```python
from openapi_client.models.delivery_options_request_order_item import DeliveryOptionsRequestOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOptionsRequestOrderItem from a JSON string
delivery_options_request_order_item_instance = DeliveryOptionsRequestOrderItem.from_json(json)
# print the JSON string representation of the object
print(DeliveryOptionsRequestOrderItem.to_json())

# convert the object into a dict
delivery_options_request_order_item_dict = delivery_options_request_order_item_instance.to_dict()
# create an instance of DeliveryOptionsRequestOrderItem from a dict
delivery_options_request_order_item_from_dict = DeliveryOptionsRequestOrderItem.from_dict(delivery_options_request_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


