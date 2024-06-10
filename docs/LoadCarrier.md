# LoadCarrier


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sscc** | **str** | The Serial Shipping Container Code (SSCC) for this load carrier. | [optional] 
**transport_label_track_and_trace** | **str** | The track and trace code for this load carrier. | [optional] 
**transport_state** | **str** | The current state of the transport for this load carrier. | 
**transport_state_update_date_time** | **datetime** | The date and time in ISO 8601 format when the latest update for this transport was received. | 

## Example

```python
from openapi_client.models.load_carrier import LoadCarrier

# TODO update the JSON string below
json = "{}"
# create an instance of LoadCarrier from a JSON string
load_carrier_instance = LoadCarrier.from_json(json)
# print the JSON string representation of the object
print(LoadCarrier.to_json())

# convert the object into a dict
load_carrier_dict = load_carrier_instance.to_dict()
# create an instance of LoadCarrier from a dict
load_carrier_from_dict = LoadCarrier.from_dict(load_carrier_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


