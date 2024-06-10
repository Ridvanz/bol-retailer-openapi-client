# ShipmentDetails

The address details where this order needs to be shipped to. This can be the customers' own address, a (company) business address or a Pick Up Point address.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pickup_point_name** | **str** | The name of Pick Up Point location this order needs to be shipped to. | [optional] 
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
**email** | **str** | A scrambled email address that can be used to contact the customer. | [optional] 
**company** | **str** | The company name. | [optional] 
**delivery_phone_number** | **str** | The delivery phone number of the customer. Filled in case the order requires an appointment for delivering the goods. | [optional] 
**language** | **str** | The language of the customer in case of contact. | [optional] 

## Example

```python
from openapi_client.models.shipment_details import ShipmentDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentDetails from a JSON string
shipment_details_instance = ShipmentDetails.from_json(json)
# print the JSON string representation of the object
print(ShipmentDetails.to_json())

# convert the object into a dict
shipment_details_dict = shipment_details_instance.to_dict()
# create an instance of ShipmentDetails from a dict
shipment_details_from_dict = ShipmentDetails.from_dict(shipment_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


