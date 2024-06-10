# ShipmentTransport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transport_id** | **str** | The transport id. | [optional] 
**transporter_code** | **str** | Specify the transporter that will carry out the shipment. | [optional] 
**track_and_trace** | **str** | The track and trace code that is associated with this transport. | 
**shipping_label_id** | **str** | The shipping label id. | [optional] 
**transport_events** | [**List[TransportEvent]**](TransportEvent.md) |  | [optional] 

## Example

```python
from openapi_client.models.shipment_transport import ShipmentTransport

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentTransport from a JSON string
shipment_transport_instance = ShipmentTransport.from_json(json)
# print the JSON string representation of the object
print(ShipmentTransport.to_json())

# convert the object into a dict
shipment_transport_dict = shipment_transport_instance.to_dict()
# create an instance of ShipmentTransport from a dict
shipment_transport_from_dict = ShipmentTransport.from_dict(shipment_transport_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


