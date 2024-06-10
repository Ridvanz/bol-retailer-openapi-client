# Product

A single product.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ean** | **str** | The EAN number associated with this product. | 
**relevance_scores** | [**List[RelevanceScore]**](RelevanceScore.md) |  | [optional] 
**maximum_price** | **float** | The maximum price a product can have in order to be part of the promotion. | [optional] 

## Example

```python
from openapi_client.models.product import Product

# TODO update the JSON string below
json = "{}"
# create an instance of Product from a JSON string
product_instance = Product.from_json(json)
# print the JSON string representation of the object
print(Product.to_json())

# convert the object into a dict
product_dict = product_instance.to_dict()
# create an instance of Product from a dict
product_from_dict = Product.from_dict(product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


