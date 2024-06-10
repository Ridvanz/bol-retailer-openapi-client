# ReplenishmentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replenishment_id** | **str** | The unique identifier of the replenishment. | 
**creation_date_time** | **datetime** | The date and time when this replenishment was created. In ISO 8601 format. | 
**reference** | **str** | Custom user defined reference to identify the replenishment. | 
**labeling_by_bol** | **bool** | Indicates whether the replenishment will be labeled by bol.com or not. | 
**state** | **str** | Indicates the state of this replenishment order. | 
**delivery_information** | [**DeliveryInformation**](DeliveryInformation.md) |  | 
**pickup_appointment** | [**PickupAppointment**](PickupAppointment.md) |  | [optional] 
**number_of_load_carriers** | **int** | The number of load carriers in this shipment. | [optional] 
**load_carriers** | [**List[LoadCarrier]**](LoadCarrier.md) |  | 
**lines** | [**List[ReplenishmentLine]**](ReplenishmentLine.md) |  | 
**invalid_lines** | [**List[InvalidReplenishmentLine]**](InvalidReplenishmentLine.md) |  | 
**state_transitions** | [**List[StateTransition]**](StateTransition.md) |  | 

## Example

```python
from openapi_client.models.replenishment_response import ReplenishmentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReplenishmentResponse from a JSON string
replenishment_response_instance = ReplenishmentResponse.from_json(json)
# print the JSON string representation of the object
print(ReplenishmentResponse.to_json())

# convert the object into a dict
replenishment_response_dict = replenishment_response_instance.to_dict()
# create an instance of ReplenishmentResponse from a dict
replenishment_response_from_dict = ReplenishmentResponse.from_dict(replenishment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


