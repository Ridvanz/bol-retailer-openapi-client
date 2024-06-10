# CreatePickupTimeSlot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_date_time** | **str** | The selected start date and time for the replenishment pickup appointment. In ISO 8601 format. | 
**until_date_time** | **str** | The selected end date and time for the replenishment pickup appointment. In ISO 8601 format. | 

## Example

```python
from openapi_client.models.create_pickup_time_slot import CreatePickupTimeSlot

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePickupTimeSlot from a JSON string
create_pickup_time_slot_instance = CreatePickupTimeSlot.from_json(json)
# print the JSON string representation of the object
print(CreatePickupTimeSlot.to_json())

# convert the object into a dict
create_pickup_time_slot_dict = create_pickup_time_slot_instance.to_dict()
# create an instance of CreatePickupTimeSlot from a dict
create_pickup_time_slot_from_dict = CreatePickupTimeSlot.from_dict(create_pickup_time_slot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


