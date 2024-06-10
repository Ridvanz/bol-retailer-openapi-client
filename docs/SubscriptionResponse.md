# SubscriptionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier assigned to each event notification subscription. This ID is used for tracking and managing each subscription. | 
**resources** | **List[str]** |  | 
**url** | **str** | The destination for event notifications. For WEBHOOK subscription types, this is the URL where messages are posted to. For GCP_PUBSUB, this is the topic name. | 
**subscription_type** | **str** | The type of subscription. It indicates the platform where the events will be subscribed to. Be aware that certain event types are only available for specific types. | 
**enabled** | **bool** | Whether the subscription is enabled and will receive notifications or not. Defaults to true. | [optional] 

## Example

```python
from openapi_client.models.subscription_response import SubscriptionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionResponse from a JSON string
subscription_response_instance = SubscriptionResponse.from_json(json)
# print the JSON string representation of the object
print(SubscriptionResponse.to_json())

# convert the object into a dict
subscription_response_dict = subscription_response_instance.to_dict()
# create an instance of SubscriptionResponse from a dict
subscription_response_from_dict = SubscriptionResponse.from_dict(subscription_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


