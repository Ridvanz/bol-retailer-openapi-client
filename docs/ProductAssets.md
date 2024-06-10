# ProductAssets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usage** | **str** | Type of the asset being used for. | 
**order** | **int** | The intended order of the product images. | 
**variants** | [**List[ProductAssetsVariants]**](ProductAssetsVariants.md) |  | 

## Example

```python
from openapi_client.models.product_assets import ProductAssets

# TODO update the JSON string below
json = "{}"
# create an instance of ProductAssets from a JSON string
product_assets_instance = ProductAssets.from_json(json)
# print the JSON string representation of the object
print(ProductAssets.to_json())

# convert the object into a dict
product_assets_dict = product_assets_instance.to_dict()
# create an instance of ProductAssets from a dict
product_assets_from_dict = ProductAssets.from_dict(product_assets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


