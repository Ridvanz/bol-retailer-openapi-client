# ProductListFilterRange

The list of range filters to get associated products for.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range_id** | **str** | The id of the range filter the products can be found within. | 
**min** | **float** | The minimum value for the range that can be used to filter the products. | 
**max** | **float** | The maximum value for the range that can be used to filter the products. | 

## Example

```python
from openapi_client.models.product_list_filter_range import ProductListFilterRange

# TODO update the JSON string below
json = "{}"
# create an instance of ProductListFilterRange from a JSON string
product_list_filter_range_instance = ProductListFilterRange.from_json(json)
# print the JSON string representation of the object
print(ProductListFilterRange.to_json())

# convert the object into a dict
product_list_filter_range_dict = product_list_filter_range_instance.to_dict()
# create an instance of ProductListFilterRange from a dict
product_list_filter_range_from_dict = ProductListFilterRange.from_dict(product_list_filter_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


