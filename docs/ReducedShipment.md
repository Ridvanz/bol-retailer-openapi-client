# ReducedShipment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_id** | **str** | A unique identifier for this shipment. | 
**shipment_date_time** | **datetime** | The date and time in ISO 8601 format when the order item was shipped. | [optional] 
**shipment_reference** | **str** | Reference supplied by the user when this item was shipped. | 
**order** | [**ReducedShipmentOrder**](ReducedShipmentOrder.md) |  | 
**shipment_items** | [**List[ReducedShipmentItem]**](ReducedShipmentItem.md) |  | 
**transport** | [**ReducedTransport**](ReducedTransport.md) |  | 

## Example

```python
from openapi_client.models.reduced_shipment import ReducedShipment

# TODO update the JSON string below
json = "{}"
# create an instance of ReducedShipment from a JSON string
reduced_shipment_instance = ReducedShipment.from_json(json)
# print the JSON string representation of the object
print(ReducedShipment.to_json())

# convert the object into a dict
reduced_shipment_dict = reduced_shipment_instance.to_dict()
# create an instance of ReducedShipment from a dict
reduced_shipment_from_dict = ReducedShipment.from_dict(reduced_shipment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


