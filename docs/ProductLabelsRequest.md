# ProductLabelsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label_format** | **str** | The printer format to create labels for. | 
**products** | [**List[ProductLabelsProduct]**](ProductLabelsProduct.md) |  | 

## Example

```python
from openapi_client.models.product_labels_request import ProductLabelsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProductLabelsRequest from a JSON string
product_labels_request_instance = ProductLabelsRequest.from_json(json)
# print the JSON string representation of the object
print(ProductLabelsRequest.to_json())

# convert the object into a dict
product_labels_request_dict = product_labels_request_instance.to_dict()
# create an instance of ProductLabelsRequest from a dict
product_labels_request_from_dict = ProductLabelsRequest.from_dict(product_labels_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


