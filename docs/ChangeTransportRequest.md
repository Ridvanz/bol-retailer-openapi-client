# ChangeTransportRequest

The change transport requested by the user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transporter_code** | **str** | Specify the transporter that carries out the shipment. | [optional] 
**track_and_trace** | **str** | The track and trace code that is associated with this transport. | 

## Example

```python
from openapi_client.models.change_transport_request import ChangeTransportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeTransportRequest from a JSON string
change_transport_request_instance = ChangeTransportRequest.from_json(json)
# print the JSON string representation of the object
print(ChangeTransportRequest.to_json())

# convert the object into a dict
change_transport_request_dict = change_transport_request_instance.to_dict()
# create an instance of ChangeTransportRequest from a dict
change_transport_request_from_dict = ChangeTransportRequest.from_dict(change_transport_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


