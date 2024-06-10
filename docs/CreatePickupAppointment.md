# CreatePickupAppointment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**CreateAddress**](CreateAddress.md) |  | 
**pickup_time_slot** | [**CreatePickupTimeSlot**](CreatePickupTimeSlot.md) |  | 
**comment_to_transporter** | **str** | A comment to the transporter regarding the pickup appointment. | [optional] 

## Example

```python
from openapi_client.models.create_pickup_appointment import CreatePickupAppointment

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePickupAppointment from a JSON string
create_pickup_appointment_instance = CreatePickupAppointment.from_json(json)
# print the JSON string representation of the object
print(CreatePickupAppointment.to_json())

# convert the object into a dict
create_pickup_appointment_dict = create_pickup_appointment_instance.to_dict()
# create an instance of CreatePickupAppointment from a dict
create_pickup_appointment_from_dict = CreatePickupAppointment.from_dict(create_pickup_appointment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


