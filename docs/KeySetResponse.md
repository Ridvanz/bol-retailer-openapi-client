# KeySetResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signature_keys** | [**List[KeySet]**](KeySet.md) |  | 

## Example

```python
from openapi_client.models.key_set_response import KeySetResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KeySetResponse from a JSON string
key_set_response_instance = KeySetResponse.from_json(json)
# print the JSON string representation of the object
print(KeySetResponse.to_json())

# convert the object into a dict
key_set_response_dict = key_set_response_instance.to_dict()
# create an instance of KeySetResponse from a dict
key_set_response_from_dict = KeySetResponse.from_dict(key_set_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


