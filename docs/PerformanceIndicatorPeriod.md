# PerformanceIndicatorPeriod

The period for which the performance is measured.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**week** | **str** | Week number in the ISO-8601 standard. | 
**year** | **str** | Year number in the ISO-8601 standard. | 

## Example

```python
from openapi_client.models.performance_indicator_period import PerformanceIndicatorPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of PerformanceIndicatorPeriod from a JSON string
performance_indicator_period_instance = PerformanceIndicatorPeriod.from_json(json)
# print the JSON string representation of the object
print(PerformanceIndicatorPeriod.to_json())

# convert the object into a dict
performance_indicator_period_dict = performance_indicator_period_instance.to_dict()
# create an instance of PerformanceIndicatorPeriod from a dict
performance_indicator_period_from_dict = PerformanceIndicatorPeriod.from_dict(performance_indicator_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


