# BillingDetails

The details of the customer that is responsible for the financial fulfillment of this order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**salutation** | **str** | The salutation of the customer. | 
**first_name** | **str** | The first name of the customer. | 
**surname** | **str** | The surname of the customer. | 
**street_name** | **str** | The street name. | 
**house_number** | **str** | The house number. | 
**house_number_extension** | **str** | The extension on the house number. | [optional] 
**extra_address_information** | **str** | Additional information related to the address that helps in delivering the package. | [optional] 
**zip_code** | **str** | The ZIP code in &#39;1234AB&#39; format for NL orders and &#39;0000&#39; format for BE orders. | 
**city** | **str** | The name of the city. | 
**country_code** | **str** | The country code. | 
**email** | **str** | A scrambled email address that can be used to contact the customer. | 
**company** | **str** | The company name. | [optional] 
**vat_number** | **str** | The Value Added Tax (VAT) / BTW number for business sellers situated in the Netherlands. | [optional] 
**kvk_number** | **str** | The Kamer van Koophandel (kvk) number for organizations situated in the Netherlands or ondernemingsnummer for organizations situated in Belgium. | [optional] 
**order_reference** | **str** | The order reference specified by the customer when ordering a product. | [optional] 

## Example

```python
from openapi_client.models.billing_details import BillingDetails

# TODO update the JSON string below
json = "{}"
# create an instance of BillingDetails from a JSON string
billing_details_instance = BillingDetails.from_json(json)
# print the JSON string representation of the object
print(BillingDetails.to_json())

# convert the object into a dict
billing_details_dict = billing_details_instance.to_dict()
# create an instance of BillingDetails from a dict
billing_details_from_dict = BillingDetails.from_dict(billing_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


