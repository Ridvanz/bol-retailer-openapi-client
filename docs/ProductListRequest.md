# ProductListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | The country for which the products will be retrieved. | [optional] [default to 'NL']
**search_term** | **str** | The search term to get the associated products for. | [optional] 
**category_id** | **str** | The category to get the associated products for. | [optional] 
**filter_ranges** | [**List[ProductListFilterRange]**](ProductListFilterRange.md) | The list of range filters to get associated products for. | [optional] 
**filter_values** | [**List[ProductListFilterValue]**](ProductListFilterValue.md) | The list of filter values in this filter. | [optional] 
**sort** | **str** | Determines the order of the products. | [optional] 
**page** | **int** | The requested page number with a page size of 50 items. | [default to 1]

## Example

```python
from openapi_client.models.product_list_request import ProductListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProductListRequest from a JSON string
product_list_request_instance = ProductListRequest.from_json(json)
# print the JSON string representation of the object
print(ProductListRequest.to_json())

# convert the object into a dict
product_list_request_dict = product_list_request_instance.to_dict()
# create an instance of ProductListRequest from a dict
product_list_request_from_dict = ProductListRequest.from_dict(product_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


