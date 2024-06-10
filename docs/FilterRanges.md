# FilterRanges

The list of range filters that is associated with the given search term or category.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range_id** | **str** | The id of the range filter product can be found under. | 
**range_name** | **str** | The name of the range filter product can be found under. | 
**min** | **float** | The minimum value for the range that can be used to filter results. | 
**max** | **float** | The maximum value for the range that can be used to filter results. | 
**unit** | **str** | The unit that applies to the min and max range values. | 

## Example

```python
from openapi_client.models.filter_ranges import FilterRanges

# TODO update the JSON string below
json = "{}"
# create an instance of FilterRanges from a JSON string
filter_ranges_instance = FilterRanges.from_json(json)
# print the JSON string representation of the object
print(FilterRanges.to_json())

# convert the object into a dict
filter_ranges_dict = filter_ranges_instance.to_dict()
# create an instance of FilterRanges from a dict
filter_ranges_from_dict = FilterRanges.from_dict(filter_ranges_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


