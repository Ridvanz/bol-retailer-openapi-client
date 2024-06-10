# PickupTimeSlot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_date_time** | **datetime** | The available start date and time for the pickup appointment. In ISO 8601 format. | 
**until_date_time** | **datetime** | The available end date and time for the pickup appointment. In ISO 8601 format. | 

## Example

```python
from openapi_client.models.pickup_time_slot import PickupTimeSlot

# TODO update the JSON string below
json = "{}"
# create an instance of PickupTimeSlot from a JSON string
pickup_time_slot_instance = PickupTimeSlot.from_json(json)
# print the JSON string representation of the object
print(PickupTimeSlot.to_json())

# convert the object into a dict
pickup_time_slot_dict = pickup_time_slot_instance.to_dict()
# create an instance of PickupTimeSlot from a dict
pickup_time_slot_from_dict = PickupTimeSlot.from_dict(pickup_time_slot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


