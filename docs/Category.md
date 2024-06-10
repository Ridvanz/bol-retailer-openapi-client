# Category


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **str** | The id of the parent category which the product belongs to. | 
**category_name** | **str** | The name of the parent category which the product belongs to. | 
**subcategories** | [**List[SubCategory]**](SubCategory.md) | The subcategories which the product belongs to. | [optional] 

## Example

```python
from openapi_client.models.category import Category

# TODO update the JSON string below
json = "{}"
# create an instance of Category from a JSON string
category_instance = Category.from_json(json)
# print the JSON string representation of the object
print(Category.to_json())

# convert the object into a dict
category_dict = category_instance.to_dict()
# create an instance of Category from a dict
category_from_dict = Category.from_dict(category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


