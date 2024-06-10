# Address


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street_name** | **str** | The street name of the pickup location. | 
**house_number** | **str** | The house number of the pickup location. | 
**house_number_extension** | **str** | The extension of the house number of the pickup location. | 
**zip_code** | **str** | The zip code in &#39;1234AB&#39; format for NL and &#39;0000&#39; for BE addresses. | 
**city** | **str** | The city of the pickup address. | 
**country_code** | **str** | The ISO 3166-2 country code. | 
**attention_of** | **str** | Name of the person responsible for this replenishment. | 

## Example

```python
from openapi_client.models.address import Address

# TODO update the JSON string below
json = "{}"
# create an instance of Address from a JSON string
address_instance = Address.from_json(json)
# print the JSON string representation of the object
print(Address.to_json())

# convert the object into a dict
address_dict = address_instance.to_dict()
# create an instance of Address from a dict
address_from_dict = Address.from_dict(address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


