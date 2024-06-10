# InvoiceRequestsBillingDetails

The details of the customer that is responsible for the financial fulfillment of this shipment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**salutation** | **str** | The salutation of the customer. | 
**first_name** | **str** | The first name of the customer. | [optional] 
**surname** | **str** | The surname of the customer. | [optional] 
**street_name** | **str** | The street name. | [optional] 
**house_number** | **str** | The house number. | [optional] 
**house_number_extension** | **str** | The extension on the house number. | [optional] 
**zip_code** | **str** | The ZIP code in &#39;1234AB&#39; format for NL orders and &#39;0000&#39; format for BE orders. | [optional] 
**city** | **str** | The name of the city. | [optional] 
**country_code** | **str** | The country code. | [optional] 
**company** | **str** | The company name. | [optional] 
**vat_number** | **str** | The Value Added Tax (VAT) / BTW number for business sellers situated in the Netherlands. | [optional] 
**kvk_number** | **str** | The Kamer van Koophandel (KvK) number for organizations situated in the Netherlands or ondernemingsnummer for organizations situated in Belgium. | [optional] 

## Example

```python
from openapi_client.models.invoice_requests_billing_details import InvoiceRequestsBillingDetails

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceRequestsBillingDetails from a JSON string
invoice_requests_billing_details_instance = InvoiceRequestsBillingDetails.from_json(json)
# print the JSON string representation of the object
print(InvoiceRequestsBillingDetails.to_json())

# convert the object into a dict
invoice_requests_billing_details_dict = invoice_requests_billing_details_instance.to_dict()
# create an instance of InvoiceRequestsBillingDetails from a dict
invoice_requests_billing_details_from_dict = InvoiceRequestsBillingDetails.from_dict(invoice_requests_billing_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


