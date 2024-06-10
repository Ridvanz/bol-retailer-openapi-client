# RequestProductDestinationsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eans** | [**List[Ean]**](Ean.md) |  | 

## Example

```python
from openapi_client.models.request_product_destinations_request import RequestProductDestinationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RequestProductDestinationsRequest from a JSON string
request_product_destinations_request_instance = RequestProductDestinationsRequest.from_json(json)
# print the JSON string representation of the object
print(RequestProductDestinationsRequest.to_json())

# convert the object into a dict
request_product_destinations_request_dict = request_product_destinations_request_instance.to_dict()
# create an instance of RequestProductDestinationsRequest from a dict
request_product_destinations_request_from_dict = RequestProductDestinationsRequest.from_dict(request_product_destinations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


