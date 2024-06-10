# ProductLabelsProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ean** | **str** | The EAN number associated with this product. | 
**quantity** | **int** | The number of products to generate labels for. | 

## Example

```python
from openapi_client.models.product_labels_product import ProductLabelsProduct

# TODO update the JSON string below
json = "{}"
# create an instance of ProductLabelsProduct from a JSON string
product_labels_product_instance = ProductLabelsProduct.from_json(json)
# print the JSON string representation of the object
print(ProductLabelsProduct.to_json())

# convert the object into a dict
product_labels_product_dict = product_labels_product_instance.to_dict()
# create an instance of ProductLabelsProduct from a dict
product_labels_product_from_dict = ProductLabelsProduct.from_dict(product_labels_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


