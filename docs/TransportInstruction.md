# TransportInstruction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transporter_code** | **str** | Specify the transporter that will carry out the shipment. | 
**track_and_trace** | **str** | The track and trace code that is associated with this transport. | [optional] 

## Example

```python
from openapi_client.models.transport_instruction import TransportInstruction

# TODO update the JSON string below
json = "{}"
# create an instance of TransportInstruction from a JSON string
transport_instruction_instance = TransportInstruction.from_json(json)
# print the JSON string representation of the object
print(TransportInstruction.to_json())

# convert the object into a dict
transport_instruction_dict = transport_instruction_instance.to_dict()
# create an instance of TransportInstruction from a dict
transport_instruction_from_dict = TransportInstruction.from_dict(transport_instruction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


