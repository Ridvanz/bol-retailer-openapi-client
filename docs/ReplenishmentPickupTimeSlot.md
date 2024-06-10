# ReplenishmentPickupTimeSlot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_date_time** | **datetime** | The selected start date and time for the replenishment pickup appointment. In ISO 8601 format. | 
**until_date_time** | **datetime** | The selected end date and time for the replenishment pickup appointment. In ISO 8601 format. | 

## Example

```python
from openapi_client.models.replenishment_pickup_time_slot import ReplenishmentPickupTimeSlot

# TODO update the JSON string below
json = "{}"
# create an instance of ReplenishmentPickupTimeSlot from a JSON string
replenishment_pickup_time_slot_instance = ReplenishmentPickupTimeSlot.from_json(json)
# print the JSON string representation of the object
print(ReplenishmentPickupTimeSlot.to_json())

# convert the object into a dict
replenishment_pickup_time_slot_dict = replenishment_pickup_time_slot_instance.to_dict()
# create an instance of ReplenishmentPickupTimeSlot from a dict
replenishment_pickup_time_slot_from_dict = ReplenishmentPickupTimeSlot.from_dict(replenishment_pickup_time_slot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


