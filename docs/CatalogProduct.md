# CatalogProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**published** | **bool** | Indicates whether the product meets the minimum requirements for publishing to the webshop. | 
**gpc** | [**Gpc**](Gpc.md) |  | 
**enrichment** | [**Enrichment**](Enrichment.md) |  | [optional] 
**attributes** | [**List[Attributes]**](Attributes.md) |  | 
**parties** | [**List[Party]**](Party.md) |  | 
**audio_tracks** | [**List[AudioTracks]**](AudioTracks.md) |  | [optional] 
**series** | [**List[Serie]**](Serie.md) |  | [optional] 

## Example

```python
from openapi_client.models.catalog_product import CatalogProduct

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogProduct from a JSON string
catalog_product_instance = CatalogProduct.from_json(json)
# print the JSON string representation of the object
print(CatalogProduct.to_json())

# convert the object into a dict
catalog_product_dict = catalog_product_instance.to_dict()
# create an instance of CatalogProduct from a dict
catalog_product_from_dict = CatalogProduct.from_dict(catalog_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


