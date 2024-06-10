# ProductIdsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bol_product_id** | **str** | Identifier of the product. This id is specific to bol.com webshop. | 
**eans** | [**List[ProductIdsEan]**](ProductIdsEan.md) |  | 

## Example

```python
from openapi_client.models.product_ids_response import ProductIdsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProductIdsResponse from a JSON string
product_ids_response_instance = ProductIdsResponse.from_json(json)
# print the JSON string representation of the object
print(ProductIdsResponse.to_json())

# convert the object into a dict
product_ids_response_dict = product_ids_response_instance.to_dict()
# create an instance of ProductIdsResponse from a dict
product_ids_response_from_dict = ProductIdsResponse.from_dict(product_ids_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


