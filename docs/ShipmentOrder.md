# ShipmentOrder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **str** | A unique identifier for the order this shipment is related to. | 
**order_placed_date_time** | **datetime** | The date and time in ISO 8601 format when the order was placed. | [optional] 

## Example

```python
from openapi_client.models.shipment_order import ShipmentOrder

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentOrder from a JSON string
shipment_order_instance = ShipmentOrder.from_json(json)
# print the JSON string representation of the object
print(ShipmentOrder.to_json())

# convert the object into a dict
shipment_order_dict = shipment_order_instance.to_dict()
# create an instance of ShipmentOrder from a dict
shipment_order_from_dict = ShipmentOrder.from_dict(shipment_order_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


