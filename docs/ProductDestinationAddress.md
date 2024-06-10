# ProductDestinationAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street_name** | **str** | The street name of the bol.com warehouse address. | 
**house_number** | **int** | The house number of the bol.com warehouse address. | 
**zip_code** | **str** | The zipcode of the bol.com warehouse address. | 
**city** | **str** | The city of the bol.com warehouse address. | 
**country_code** | **str** | The ISO 3166-2 country code of the bol.com warehouse address. | 
**attention_of** | **str** | Name of the person responsible for this replenishment. | 
**house_number_extension** | **str** | The house number extension of the bol.com warehouse address. | [optional] 

## Example

```python
from openapi_client.models.product_destination_address import ProductDestinationAddress

# TODO update the JSON string below
json = "{}"
# create an instance of ProductDestinationAddress from a JSON string
product_destination_address_instance = ProductDestinationAddress.from_json(json)
# print the JSON string representation of the object
print(ProductDestinationAddress.to_json())

# convert the object into a dict
product_destination_address_dict = product_destination_address_instance.to_dict()
# create an instance of ProductDestinationAddress from a dict
product_destination_address_from_dict = ProductDestinationAddress.from_dict(product_destination_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


