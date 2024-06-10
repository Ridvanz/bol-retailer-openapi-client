# UpdateReplenishmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | Update the state of the replenishment to cancel the replenishment. | [optional] 
**delivery_info** | [**UpdateDeliveryInfo**](UpdateDeliveryInfo.md) |  | [optional] 
**number_of_load_carriers** | **int** | The number of parcels in this replenishment. Note: if you are using the bol.com pickup service, the maximum number is 20. | [optional] 
**load_carriers** | [**List[UpdateLoadCarrier]**](UpdateLoadCarrier.md) |  | [optional] 

## Example

```python
from openapi_client.models.update_replenishment_request import UpdateReplenishmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateReplenishmentRequest from a JSON string
update_replenishment_request_instance = UpdateReplenishmentRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateReplenishmentRequest.to_json())

# convert the object into a dict
update_replenishment_request_dict = update_replenishment_request_instance.to_dict()
# create an instance of UpdateReplenishmentRequest from a dict
update_replenishment_request_from_dict = UpdateReplenishmentRequest.from_dict(update_replenishment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


