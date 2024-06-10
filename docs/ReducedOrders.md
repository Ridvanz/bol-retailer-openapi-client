# ReducedOrders

Container for many orders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**orders** | [**List[ReducedOrder]**](ReducedOrder.md) |  | 

## Example

```python
from openapi_client.models.reduced_orders import ReducedOrders

# TODO update the JSON string below
json = "{}"
# create an instance of ReducedOrders from a JSON string
reduced_orders_instance = ReducedOrders.from_json(json)
# print the JSON string representation of the object
print(ReducedOrders.to_json())

# convert the object into a dict
reduced_orders_dict = reduced_orders_instance.to_dict()
# create an instance of ReducedOrders from a dict
reduced_orders_from_dict = ReducedOrders.from_dict(reduced_orders_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


