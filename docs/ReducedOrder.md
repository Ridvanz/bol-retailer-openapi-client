# ReducedOrder

An order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | The identifier of the order. | 
**order_placed_date_time** | **datetime** | The date and time in ISO 8601 format when the order was placed. | 
**order_items** | [**List[ReducedOrderItem]**](ReducedOrderItem.md) |  | 

## Example

```python
from openapi_client.models.reduced_order import ReducedOrder

# TODO update the JSON string below
json = "{}"
# create an instance of ReducedOrder from a JSON string
reduced_order_instance = ReducedOrder.from_json(json)
# print the JSON string representation of the object
print(ReducedOrder.to_json())

# convert the object into a dict
reduced_order_dict = reduced_order_instance.to_dict()
# create an instance of ReducedOrder from a dict
reduced_order_from_dict = ReducedOrder.from_dict(reduced_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


