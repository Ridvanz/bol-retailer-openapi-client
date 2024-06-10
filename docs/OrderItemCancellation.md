# OrderItemCancellation

List of order items to cancel. Order item id's must belong to the same order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_item_id** | **str** | The id for the order item. One order can have multiple order items, but the list can only take one item. | 
**reason_code** | **str** | The code representing the reason for cancellation of this item. | 

## Example

```python
from openapi_client.models.order_item_cancellation import OrderItemCancellation

# TODO update the JSON string below
json = "{}"
# create an instance of OrderItemCancellation from a JSON string
order_item_cancellation_instance = OrderItemCancellation.from_json(json)
# print the JSON string representation of the object
print(OrderItemCancellation.to_json())

# convert the object into a dict
order_item_cancellation_dict = order_item_cancellation_instance.to_dict()
# create an instance of OrderItemCancellation from a dict
order_item_cancellation_from_dict = OrderItemCancellation.from_dict(order_item_cancellation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


