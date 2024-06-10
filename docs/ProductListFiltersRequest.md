# ProductListFiltersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_term** | **str** |  | [optional] 
**category_id** | **str** |  | [optional] 
**search** | **str** |  | [optional] 
**category** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.product_list_filters_request import ProductListFiltersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProductListFiltersRequest from a JSON string
product_list_filters_request_instance = ProductListFiltersRequest.from_json(json)
# print the JSON string representation of the object
print(ProductListFiltersRequest.to_json())

# convert the object into a dict
product_list_filters_request_dict = product_list_filters_request_instance.to_dict()
# create an instance of ProductListFiltersRequest from a dict
product_list_filters_request_from_dict = ProductListFiltersRequest.from_dict(product_list_filters_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


