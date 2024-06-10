# DestinationWarehouse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street_name** | **str** | The street name of the pickup address. | 
**house_number** | **str** | The house number of the pickup address. | 
**house_number_extension** | **str** | The extension of the house number. | 
**zip_code** | **str** | The zip code in &#39;1234AB&#39; format for NL and &#39;0000&#39; for BE addresses. | 
**city** | **str** | The city of the pickup address. | 
**country_code** | **str** | The ISO 3166-2 country code. | 
**attention_of** | **str** | Name of the person responsible for this replenishment. | 

## Example

```python
from openapi_client.models.destination_warehouse import DestinationWarehouse

# TODO update the JSON string below
json = "{}"
# create an instance of DestinationWarehouse from a JSON string
destination_warehouse_instance = DestinationWarehouse.from_json(json)
# print the JSON string representation of the object
print(DestinationWarehouse.to_json())

# convert the object into a dict
destination_warehouse_dict = destination_warehouse_instance.to_dict()
# create an instance of DestinationWarehouse from a dict
destination_warehouse_from_dict = DestinationWarehouse.from_dict(destination_warehouse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


