# ProductListFilterValue

The list of filter values in this filter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filter_value_id** | **str** | The unique identifier of the filter value. | 

## Example

```python
from openapi_client.models.product_list_filter_value import ProductListFilterValue

# TODO update the JSON string below
json = "{}"
# create an instance of ProductListFilterValue from a JSON string
product_list_filter_value_instance = ProductListFilterValue.from_json(json)
# print the JSON string representation of the object
print(ProductListFilterValue.to_json())

# convert the object into a dict
product_list_filter_value_dict = product_list_filter_value_instance.to_dict()
# create an instance of ProductListFilterValue from a dict
product_list_filter_value_from_dict = ProductListFilterValue.from_dict(product_list_filter_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


