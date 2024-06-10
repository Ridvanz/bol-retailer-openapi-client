# ProductAssetsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**List[ProductAssets]**](ProductAssets.md) |  | 

## Example

```python
from openapi_client.models.product_assets_response import ProductAssetsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProductAssetsResponse from a JSON string
product_assets_response_instance = ProductAssetsResponse.from_json(json)
# print the JSON string representation of the object
print(ProductAssetsResponse.to_json())

# convert the object into a dict
product_assets_response_dict = product_assets_response_instance.to_dict()
# create an instance of ProductAssetsResponse from a dict
product_assets_response_from_dict = ProductAssetsResponse.from_dict(product_assets_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


