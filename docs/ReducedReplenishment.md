# ReducedReplenishment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replenishment_id** | **str** | The unique identifier of the replenishment. | 
**reference** | **str** | Custom user defined reference to identify the replenishment. | 
**creation_date_time** | **datetime** | The date and time when this replenishment was created. In ISO 8601 format. | 
**lines** | [**List[ReducedReplenishmentLines]**](ReducedReplenishmentLines.md) |  | 
**invalid_lines** | [**List[ReducedInvalidReplenishmentLine]**](ReducedInvalidReplenishmentLine.md) |  | 

## Example

```python
from openapi_client.models.reduced_replenishment import ReducedReplenishment

# TODO update the JSON string below
json = "{}"
# create an instance of ReducedReplenishment from a JSON string
reduced_replenishment_instance = ReducedReplenishment.from_json(json)
# print the JSON string representation of the object
print(ReducedReplenishment.to_json())

# convert the object into a dict
reduced_replenishment_dict = reduced_replenishment_instance.to_dict()
# create an instance of ReducedReplenishment from a dict
reduced_replenishment_from_dict = ReducedReplenishment.from_dict(reduced_replenishment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


