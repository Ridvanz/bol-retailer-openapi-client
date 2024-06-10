# Order

An order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | The identifier of the order. | 
**pickup_point** | **bool** | Indicates whether this order is shipped to a Pick Up Point. | 
**order_placed_date_time** | **datetime** | The date and time in ISO 8601 format when the order was placed. | [optional] 
**shipment_details** | [**ShipmentDetails**](ShipmentDetails.md) |  | 
**billing_details** | [**BillingDetails**](BillingDetails.md) |  | [optional] 
**order_items** | [**List[OrderOrderItem]**](OrderOrderItem.md) |  | 

## Example

```python
from openapi_client.models.order import Order

# TODO update the JSON string below
json = "{}"
# create an instance of Order from a JSON string
order_instance = Order.from_json(json)
# print the JSON string representation of the object
print(Order.to_json())

# convert the object into a dict
order_dict = order_instance.to_dict()
# create an instance of Order from a dict
order_from_dict = Order.from_dict(order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


