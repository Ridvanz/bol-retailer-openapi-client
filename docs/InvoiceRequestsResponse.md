# InvoiceRequestsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice_requests** | [**List[InvoiceRequests]**](InvoiceRequests.md) |  | 

## Example

```python
from openapi_client.models.invoice_requests_response import InvoiceRequestsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceRequestsResponse from a JSON string
invoice_requests_response_instance = InvoiceRequestsResponse.from_json(json)
# print the JSON string representation of the object
print(InvoiceRequestsResponse.to_json())

# convert the object into a dict
invoice_requests_response_dict = invoice_requests_response_instance.to_dict()
# create an instance of InvoiceRequestsResponse from a dict
invoice_requests_response_from_dict = InvoiceRequestsResponse.from_dict(invoice_requests_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


