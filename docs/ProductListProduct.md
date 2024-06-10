# ProductListProduct

The list of products that is associated with the given search term or category and filters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The title of the product. | 
**eans** | [**List[ProductListProductEan]**](ProductListProductEan.md) |  | 

## Example

```python
from openapi_client.models.product_list_product import ProductListProduct

# TODO update the JSON string below
json = "{}"
# create an instance of ProductListProduct from a JSON string
product_list_product_instance = ProductListProduct.from_json(json)
# print the JSON string representation of the object
print(ProductListProduct.to_json())

# convert the object into a dict
product_list_product_dict = product_list_product_instance.to_dict()
# create an instance of ProductListProduct from a dict
product_list_product_from_dict = ProductListProduct.from_dict(product_list_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


