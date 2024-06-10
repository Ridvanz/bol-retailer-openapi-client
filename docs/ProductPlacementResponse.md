# ProductPlacementResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL of the product on the webshop. | 
**categories** | [**List[Category]**](Category.md) |  | 

## Example

```python
from openapi_client.models.product_placement_response import ProductPlacementResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProductPlacementResponse from a JSON string
product_placement_response_instance = ProductPlacementResponse.from_json(json)
# print the JSON string representation of the object
print(ProductPlacementResponse.to_json())

# convert the object into a dict
product_placement_response_dict = product_placement_response_instance.to_dict()
# create an instance of ProductPlacementResponse from a dict
product_placement_response_from_dict = ProductPlacementResponse.from_dict(product_placement_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


