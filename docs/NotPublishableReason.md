# NotPublishableReason


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Error code signalling that the offer is invalid. | 
**description** | **str** | Error message describing the reason the offer is invalid. | 

## Example

```python
from openapi_client.models.not_publishable_reason import NotPublishableReason

# TODO update the JSON string below
json = "{}"
# create an instance of NotPublishableReason from a JSON string
not_publishable_reason_instance = NotPublishableReason.from_json(json)
# print the JSON string representation of the object
print(NotPublishableReason.to_json())

# convert the object into a dict
not_publishable_reason_dict = not_publishable_reason_instance.to_dict()
# create an instance of NotPublishableReason from a dict
not_publishable_reason_from_dict = NotPublishableReason.from_dict(not_publishable_reason_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


