# Shipment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_id** | **str** | A unique identifier for this shipment. | 
**shipment_date_time** | **datetime** | The date and time in ISO 8601 format when the order item was shipped. | [optional] 
**shipment_reference** | **str** | Reference supplied by the user when this item was shipped. | 
**pickup_point** | **bool** | Indicates whether this order is shipped to a Pick Up Point. | [optional] 
**order** | [**ShipmentOrder**](ShipmentOrder.md) |  | 
**shipment_details** | [**ShipmentDetails**](ShipmentDetails.md) |  | [optional] 
**billing_details** | [**BillingDetails**](BillingDetails.md) |  | [optional] 
**shipment_items** | [**List[ShipmentItem]**](ShipmentItem.md) |  | 
**transport** | [**ShipmentTransport**](ShipmentTransport.md) |  | [optional] 

## Example

```python
from openapi_client.models.shipment import Shipment

# TODO update the JSON string below
json = "{}"
# create an instance of Shipment from a JSON string
shipment_instance = Shipment.from_json(json)
# print the JSON string representation of the object
print(Shipment.to_json())

# convert the object into a dict
shipment_dict = shipment_instance.to_dict()
# create an instance of Shipment from a dict
shipment_from_dict = Shipment.from_dict(shipment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


