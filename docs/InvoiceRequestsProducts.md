# InvoiceRequestsProducts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The description of the ordered product. | [optional] 
**quantity** | **int** | Amount of the product being ordered. | [optional] 
**unit_price** | **float** | The selling price to the customer of a single unit including VAT. | [optional] 

## Example

```python
from openapi_client.models.invoice_requests_products import InvoiceRequestsProducts

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceRequestsProducts from a JSON string
invoice_requests_products_instance = InvoiceRequestsProducts.from_json(json)
# print the JSON string representation of the object
print(InvoiceRequestsProducts.to_json())

# convert the object into a dict
invoice_requests_products_dict = invoice_requests_products_instance.to_dict()
# create an instance of InvoiceRequestsProducts from a dict
invoice_requests_products_from_dict = InvoiceRequestsProducts.from_dict(invoice_requests_products_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


