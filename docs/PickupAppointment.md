# PickupAppointment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**comment_to_transporter** | **str** | A comment to the transporter regarding the pickup appointment. | [optional] 
**address** | [**Address**](Address.md) |  | 
**pickup_time_slot** | [**ReplenishmentPickupTimeSlot**](ReplenishmentPickupTimeSlot.md) |  | 
**pickup_date_time** | **datetime** | The date and time in ISO 8601 format when this replenishment was picked up by the transporter. | [optional] 
**cancellation_reason** | **str** | In case of a pickup cancellation this field indicates the reason for cancelling this pickup. | [optional] 

## Example

```python
from openapi_client.models.pickup_appointment import PickupAppointment

# TODO update the JSON string below
json = "{}"
# create an instance of PickupAppointment from a JSON string
pickup_appointment_instance = PickupAppointment.from_json(json)
# print the JSON string representation of the object
print(PickupAppointment.to_json())

# convert the object into a dict
pickup_appointment_dict = pickup_appointment_instance.to_dict()
# create an instance of PickupAppointment from a dict
pickup_appointment_from_dict = PickupAppointment.from_dict(pickup_appointment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


