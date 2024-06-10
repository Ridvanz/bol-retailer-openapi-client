# PerformanceIndicator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Indicator name. | 
**type** | **str** | Interpretation of the data that applies to this measurement. | 
**details** | [**Details**](Details.md) |  | 

## Example

```python
from openapi_client.models.performance_indicator import PerformanceIndicator

# TODO update the JSON string below
json = "{}"
# create an instance of PerformanceIndicator from a JSON string
performance_indicator_instance = PerformanceIndicator.from_json(json)
# print the JSON string representation of the object
print(PerformanceIndicator.to_json())

# convert the object into a dict
performance_indicator_dict = performance_indicator_instance.to_dict()
# create an instance of PerformanceIndicator from a dict
performance_indicator_from_dict = PerformanceIndicator.from_dict(performance_indicator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


