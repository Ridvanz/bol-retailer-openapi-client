# CreateAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street_name** | **str** | The street name of the pickup address. | 
**house_number** | **str** | The house number of the pickup address. | 
**zip_code** | **str** | The zip code in &#39;1234AB&#39; format for NL and &#39;0000&#39; for BE addresses. | 
**house_number_extension** | **str** | The extension of the house number. | [optional] 
**city** | **str** | The city of the pickup address. | 
**country_code** | **str** | The ISO 3166-2 country code. | 
**attention_of** | **str** | Name of the person responsible for this replenishment. | 

## Example

```python
from openapi_client.models.create_address import CreateAddress

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAddress from a JSON string
create_address_instance = CreateAddress.from_json(json)
# print the JSON string representation of the object
print(CreateAddress.to_json())

# convert the object into a dict
create_address_dict = create_address_instance.to_dict()
# create an instance of CreateAddress from a dict
create_address_from_dict = CreateAddress.from_dict(create_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


