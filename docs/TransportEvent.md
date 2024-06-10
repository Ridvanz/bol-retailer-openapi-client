# TransportEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_code** | **str** | The transport event code indicates the location of the parcel within the distribution process. | 
**event_date_time** | **datetime** | The date time of the transport event. | 

## Example

```python
from openapi_client.models.transport_event import TransportEvent

# TODO update the JSON string below
json = "{}"
# create an instance of TransportEvent from a JSON string
transport_event_instance = TransportEvent.from_json(json)
# print the JSON string representation of the object
print(TransportEvent.to_json())

# convert the object into a dict
transport_event_dict = transport_event_instance.to_dict()
# create an instance of TransportEvent from a dict
transport_event_from_dict = TransportEvent.from_dict(transport_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


