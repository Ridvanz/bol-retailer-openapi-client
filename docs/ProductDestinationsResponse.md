# ProductDestinationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_destinations** | [**List[ProductDestination]**](ProductDestination.md) |  | 

## Example

```python
from openapi_client.models.product_destinations_response import ProductDestinationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProductDestinationsResponse from a JSON string
product_destinations_response_instance = ProductDestinationsResponse.from_json(json)
# print the JSON string representation of the object
print(ProductDestinationsResponse.to_json())

# convert the object into a dict
product_destinations_response_dict = product_destinations_response_instance.to_dict()
# create an instance of ProductDestinationsResponse from a dict
product_destinations_response_from_dict = ProductDestinationsResponse.from_dict(product_destinations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


