# CustomerDetails

Information related to the customer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**salutation** | **str** | The salutation of the customer. | 
**first_name** | **str** | The first name of the customer. | [optional] 
**surname** | **str** | The surname of the customer. | [optional] 
**street_name** | **str** | The street name. | [optional] 
**house_number** | **str** | The house number. | [optional] 
**house_number_extension** | **str** | The extension on the house number. | [optional] 
**extra_address_information** | **str** | Additional information related to the address that helps in delivering the package. | [optional] 
**zip_code** | **str** | The ZIP code in &#39;1234AB&#39; format for NL orders and &#39;0000&#39; format for BE orders. | [optional] 
**city** | **str** | The name of the city. | [optional] 
**country_code** | **str** | The country code. | [optional] 
**email** | **str** | A scrambled email address that can be used to contact the customer. | [optional] 
**delivery_phone_number** | **str** | The delivery phone number of the customer. Filled in case the order requires an appointment for delivering the goods. | [optional] 
**company** | **str** | The company name. | [optional] 
**vat_number** | **str** | The Value Added Tax (VAT) / BTW number for business sellers situated in the Netherlands. | [optional] 

## Example

```python
from openapi_client.models.customer_details import CustomerDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerDetails from a JSON string
customer_details_instance = CustomerDetails.from_json(json)
# print the JSON string representation of the object
print(CustomerDetails.to_json())

# convert the object into a dict
customer_details_dict = customer_details_instance.to_dict()
# create an instance of CustomerDetails from a dict
customer_details_from_dict = CustomerDetails.from_dict(customer_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


