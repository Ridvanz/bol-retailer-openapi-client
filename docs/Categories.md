# Categories

The list of categories that are available to further narrow down search results, for the given search term and category.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_name** | **str** | The name of the categories. | 
**category_values** | [**List[CategoryValues]**](CategoryValues.md) | The list of available categories. | 

## Example

```python
from openapi_client.models.categories import Categories

# TODO update the JSON string below
json = "{}"
# create an instance of Categories from a JSON string
categories_instance = Categories.from_json(json)
# print the JSON string representation of the object
print(Categories.to_json())

# convert the object into a dict
categories_dict = categories_instance.to_dict()
# create an instance of Categories from a dict
categories_from_dict = Categories.from_dict(categories_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


