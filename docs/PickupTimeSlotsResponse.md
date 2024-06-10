# PickupTimeSlotsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_slots** | [**List[PickupTimeSlot]**](PickupTimeSlot.md) |  | [optional] 

## Example

```python
from openapi_client.models.pickup_time_slots_response import PickupTimeSlotsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PickupTimeSlotsResponse from a JSON string
pickup_time_slots_response_instance = PickupTimeSlotsResponse.from_json(json)
# print the JSON string representation of the object
print(PickupTimeSlotsResponse.to_json())

# convert the object into a dict
pickup_time_slots_response_dict = pickup_time_slots_response_instance.to_dict()
# create an instance of PickupTimeSlotsResponse from a dict
pickup_time_slots_response_from_dict = PickupTimeSlotsResponse.from_dict(pickup_time_slots_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


