# ProductListFiltersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_data** | [**Categories**](Categories.md) |  | 
**filter_ranges** | [**List[FilterRanges]**](FilterRanges.md) | The list of range filters that is associated with the given search term or category. | 
**filters** | [**List[Filters]**](Filters.md) | The list of filters that is associated with the given search term or category. | 

## Example

```python
from openapi_client.models.product_list_filters_response import ProductListFiltersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProductListFiltersResponse from a JSON string
product_list_filters_response_instance = ProductListFiltersResponse.from_json(json)
# print the JSON string representation of the object
print(ProductListFiltersResponse.to_json())

# convert the object into a dict
product_list_filters_response_dict = product_list_filters_response_instance.to_dict()
# create an instance of ProductListFiltersResponse from a dict
product_list_filters_response_from_dict = ProductListFiltersResponse.from_dict(product_list_filters_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


