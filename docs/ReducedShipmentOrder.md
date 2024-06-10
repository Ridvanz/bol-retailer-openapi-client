# ReducedShipmentOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | A unique identifier for the order this shipment is related to. | 
**order_placed_date_time** | **datetime** | The date and time in ISO 8601 format when the order was placed. | [optional] 

## Example

```python
from openapi_client.models.reduced_shipment_order import ReducedShipmentOrder

# TODO update the JSON string below
json = "{}"
# create an instance of ReducedShipmentOrder from a JSON string
reduced_shipment_order_instance = ReducedShipmentOrder.from_json(json)
# print the JSON string representation of the object
print(ReducedShipmentOrder.to_json())

# convert the object into a dict
reduced_shipment_order_dict = reduced_shipment_order_instance.to_dict()
# create an instance of ReducedShipmentOrder from a dict
reduced_shipment_order_from_dict = ReducedShipmentOrder.from_dict(reduced_shipment_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


