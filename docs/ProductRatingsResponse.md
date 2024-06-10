# ProductRatingsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ratings** | [**List[ProductRatingsRating]**](ProductRatingsRating.md) |  | 

## Example

```python
from openapi_client.models.product_ratings_response import ProductRatingsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProductRatingsResponse from a JSON string
product_ratings_response_instance = ProductRatingsResponse.from_json(json)
# print the JSON string representation of the object
print(ProductRatingsResponse.to_json())

# convert the object into a dict
product_ratings_response_dict = product_ratings_response_instance.to_dict()
# create an instance of ProductRatingsResponse from a dict
product_ratings_response_from_dict = ProductRatingsResponse.from_dict(product_ratings_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


