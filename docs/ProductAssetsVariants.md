# ProductAssetsVariants


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **str** | The name of the size of the asset, if the asset is an image. | 
**width** | **int** | The width of the asset in pixels. | 
**height** | **int** | The height of the asset in pixels. | 
**mime_type** | **str** | The mime type of the asset. | 
**url** | **str** | The URL of the attribute. | 

## Example

```python
from openapi_client.models.product_assets_variants import ProductAssetsVariants

# TODO update the JSON string below
json = "{}"
# create an instance of ProductAssetsVariants from a JSON string
product_assets_variants_instance = ProductAssetsVariants.from_json(json)
# print the JSON string representation of the object
print(ProductAssetsVariants.to_json())

# convert the object into a dict
product_assets_variants_dict = product_assets_variants_instance.to_dict()
# create an instance of ProductAssetsVariants from a dict
product_assets_variants_from_dict = ProductAssetsVariants.from_dict(product_assets_variants_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


