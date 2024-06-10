# InvoiceRequests


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipment_id** | **str** | The id of the shipment associated with this invoice request. | 
**order_id** | **str** | The id of the order associated with this shipment. | [optional] 
**customer_account_number** | **str** | The account of the customer within bol.com associated with this shipment. | [optional] 
**billing_details** | [**InvoiceRequestsBillingDetails**](InvoiceRequestsBillingDetails.md) |  | [optional] 
**products** | [**List[InvoiceRequestsProducts]**](InvoiceRequestsProducts.md) |  | [optional] 
**status** | **str** | The current status of the invoice request. | 
**status_transitions** | [**List[StatusTransitions]**](StatusTransitions.md) |  | 

## Example

```python
from openapi_client.models.invoice_requests import InvoiceRequests

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceRequests from a JSON string
invoice_requests_instance = InvoiceRequests.from_json(json)
# print the JSON string representation of the object
print(InvoiceRequests.to_json())

# convert the object into a dict
invoice_requests_dict = invoice_requests_instance.to_dict()
# create an instance of InvoiceRequests from a dict
invoice_requests_from_dict = InvoiceRequests.from_dict(invoice_requests_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


