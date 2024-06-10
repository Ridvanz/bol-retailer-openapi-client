# PerformanceIndicators


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**performance_indicators** | [**List[PerformanceIndicator]**](PerformanceIndicator.md) |  | 

## Example

```python
from openapi_client.models.performance_indicators import PerformanceIndicators

# TODO update the JSON string below
json = "{}"
# create an instance of PerformanceIndicators from a JSON string
performance_indicators_instance = PerformanceIndicators.from_json(json)
# print the JSON string representation of the object
print(PerformanceIndicators.to_json())

# convert the object into a dict
performance_indicators_dict = performance_indicators_instance.to_dict()
# create an instance of PerformanceIndicators from a dict
performance_indicators_from_dict = PerformanceIndicators.from_dict(performance_indicators_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


