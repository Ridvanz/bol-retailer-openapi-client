# Party


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the party involved for this product. | 
**type** | **str** | The type of party involved for this product. | 
**role** | **str** | The role of the party involved for this product. | 

## Example

```python
from openapi_client.models.party import Party

# TODO update the JSON string below
json = "{}"
# create an instance of Party from a JSON string
party_instance = Party.from_json(json)
# print the JSON string representation of the object
print(Party.to_json())

# convert the object into a dict
party_dict = party_instance.to_dict()
# create an instance of Party from a dict
party_from_dict = Party.from_dict(party_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


