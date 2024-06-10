# CreateReplenishmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference** | **str** | Custom user reference for this replenishment. Must contain at least 1 digit and only upper case characters allowed. | 
**delivery_info** | [**CreateDeliveryInfo**](CreateDeliveryInfo.md) |  | [optional] 
**labeling_by_bol** | **bool** | Indicates whether the replenishment will be labeled by bol.com. | 
**number_of_load_carriers** | **int** | The number of parcels in this replenishment. Note: if you are using the bol.com pickup service, the maximum number is 20. | 
**pickup_appointment** | [**CreatePickupAppointment**](CreatePickupAppointment.md) |  | [optional] 
**lines** | [**List[CreateReplenishmentLine]**](CreateReplenishmentLine.md) |  | 

## Example

```python
from openapi_client.models.create_replenishment_request import CreateReplenishmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateReplenishmentRequest from a JSON string
create_replenishment_request_instance = CreateReplenishmentRequest.from_json(json)
# print the JSON string representation of the object
print(CreateReplenishmentRequest.to_json())

# convert the object into a dict
create_replenishment_request_dict = create_replenishment_request_instance.to_dict()
# create an instance of CreateReplenishmentRequest from a dict
create_replenishment_request_from_dict = CreateReplenishmentRequest.from_dict(create_replenishment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


