# FilterValues

The list of filter values in this filter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_value_id** | **str** | The unique identifier of the filter value. | 
**filter_value_name** | **str** | The name of the filter value. | [optional] 

## Example

```python
from openapi_client.models.filter_values import FilterValues

# TODO update the JSON string below
json = "{}"
# create an instance of FilterValues from a JSON string
filter_values_instance = FilterValues.from_json(json)
# print the JSON string representation of the object
print(FilterValues.to_json())

# convert the object into a dict
filter_values_dict = filter_values_instance.to_dict()
# create an instance of FilterValues from a dict
filter_values_from_dict = FilterValues.from_dict(filter_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


