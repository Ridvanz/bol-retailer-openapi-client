# KeySet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Key identifier. Maps to the keyId value in the signature header of the push request. | 
**type** | **str** | Key encryption type. | 
**public_key** | **str** | The Base64 encoded public key to use when verifying the signature. | 

## Example

```python
from openapi_client.models.key_set import KeySet

# TODO update the JSON string below
json = "{}"
# create an instance of KeySet from a JSON string
key_set_instance = KeySet.from_json(json)
# print the JSON string representation of the object
print(KeySet.to_json())

# convert the object into a dict
key_set_dict = key_set_instance.to_dict()
# create an instance of KeySet from a dict
key_set_from_dict = KeySet.from_dict(key_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


