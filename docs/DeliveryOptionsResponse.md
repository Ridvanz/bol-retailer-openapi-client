# DeliveryOptionsResponse

The possible delivery options based on a shippable configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_options** | [**List[DeliveryOption]**](DeliveryOption.md) |  | 

## Example

```python
from openapi_client.models.delivery_options_response import DeliveryOptionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOptionsResponse from a JSON string
delivery_options_response_instance = DeliveryOptionsResponse.from_json(json)
# print the JSON string representation of the object
print(DeliveryOptionsResponse.to_json())

# convert the object into a dict
delivery_options_response_dict = delivery_options_response_instance.to_dict()
# create an instance of DeliveryOptionsResponse from a dict
delivery_options_response_from_dict = DeliveryOptionsResponse.from_dict(delivery_options_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


