# TotalPeriod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | [**SearchTermsPeriod**](SearchTermsPeriod.md) |  | 
**total** | **int** | The number of customer visits on the search page. | 
**countries** | [**List[SearchTermsCountry]**](SearchTermsCountry.md) |  | 

## Example

```python
from openapi_client.models.total_period import TotalPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of TotalPeriod from a JSON string
total_period_instance = TotalPeriod.from_json(json)
# print the JSON string representation of the object
print(TotalPeriod.to_json())

# convert the object into a dict
total_period_dict = total_period_instance.to_dict()
# create an instance of TotalPeriod from a dict
total_period_from_dict = TotalPeriod.from_dict(total_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


