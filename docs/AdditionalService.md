# AdditionalService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_type** | **str** | An additional service type that the customer selected when purchasing this order item. | 

## Example

```python
from openapi_client.models.additional_service import AdditionalService

# TODO update the JSON string below
json = "{}"
# create an instance of AdditionalService from a JSON string
additional_service_instance = AdditionalService.from_json(json)
# print the JSON string representation of the object
print(AdditionalService.to_json())

# convert the object into a dict
additional_service_dict = additional_service_instance.to_dict()
# create an instance of AdditionalService from a dict
additional_service_from_dict = AdditionalService.from_dict(additional_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


