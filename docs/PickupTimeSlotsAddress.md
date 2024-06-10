# PickupTimeSlotsAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street_name** | **str** | The street name of the pickup address. | 
**house_number** | **str** | The house number of the pickup address. | 
**house_number_extension** | **str** | The extension of the house number. | [optional] 
**zip_code** | **str** | The zip code in &#39;1234AB&#39; format for NL and &#39;0000&#39; for BE addresses. | 
**city** | **str** | The city of the pickup address. | 
**country_code** | **str** | The ISO 3166-2 country code. | 

## Example

```python
from openapi_client.models.pickup_time_slots_address import PickupTimeSlotsAddress

# TODO update the JSON string below
json = "{}"
# create an instance of PickupTimeSlotsAddress from a JSON string
pickup_time_slots_address_instance = PickupTimeSlotsAddress.from_json(json)
# print the JSON string representation of the object
print(PickupTimeSlotsAddress.to_json())

# convert the object into a dict
pickup_time_slots_address_dict = pickup_time_slots_address_instance.to_dict()
# create an instance of PickupTimeSlotsAddress from a dict
pickup_time_slots_address_from_dict = PickupTimeSlotsAddress.from_dict(pickup_time_slots_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


