# SubscriptionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscriptions** | [**List[SubscriptionResponse]**](SubscriptionResponse.md) |  | 

## Example

```python
from openapi_client.models.subscriptions_response import SubscriptionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionsResponse from a JSON string
subscriptions_response_instance = SubscriptionsResponse.from_json(json)
# print the JSON string representation of the object
print(SubscriptionsResponse.to_json())

# convert the object into a dict
subscriptions_response_dict = subscriptions_response_instance.to_dict()
# create an instance of SubscriptionsResponse from a dict
subscriptions_response_from_dict = SubscriptionsResponse.from_dict(subscriptions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


