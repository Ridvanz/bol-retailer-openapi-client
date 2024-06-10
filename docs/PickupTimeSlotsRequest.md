# PickupTimeSlotsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**PickupTimeSlotsAddress**](PickupTimeSlotsAddress.md) |  | 
**number_of_load_carriers** | **int** | The number of load carriers in this shipment. | 

## Example

```python
from openapi_client.models.pickup_time_slots_request import PickupTimeSlotsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PickupTimeSlotsRequest from a JSON string
pickup_time_slots_request_instance = PickupTimeSlotsRequest.from_json(json)
# print the JSON string representation of the object
print(PickupTimeSlotsRequest.to_json())

# convert the object into a dict
pickup_time_slots_request_dict = pickup_time_slots_request_instance.to_dict()
# create an instance of PickupTimeSlotsRequest from a dict
pickup_time_slots_request_from_dict = PickupTimeSlotsRequest.from_dict(pickup_time_slots_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


