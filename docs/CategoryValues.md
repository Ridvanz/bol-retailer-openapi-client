# CategoryValues

The list of available categories.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_value_id** | **str** | The id of the category. This id can be used in other endpoints, like Get product list. | [optional] 
**category_value_name** | **str** | The name of the category. | [optional] 

## Example

```python
from openapi_client.models.category_values import CategoryValues

# TODO update the JSON string below
json = "{}"
# create an instance of CategoryValues from a JSON string
category_values_instance = CategoryValues.from_json(json)
# print the JSON string representation of the object
print(CategoryValues.to_json())

# convert the object into a dict
category_values_dict = category_values_instance.to_dict()
# create an instance of CategoryValues from a dict
category_values_from_dict = CategoryValues.from_dict(category_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


