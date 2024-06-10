# SubscriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resources** | **List[str]** | Array of event types for which the subscription is set. Note that some event types are only available for certain subscription types. | 
**url** | **str** | The destination for event notifications. For WEBHOOK subscription types, this is the URL where messages are posted to. For GCP_PUBSUB, this is the topic name. | 
**subscription_type** | **str** | The type of subscription. It indicates the platform where the events will be subscribed to. Be aware that certain event types are only available for specific types. | 
**enabled** | **bool** | Whether the subscription is enabled and will receive notifications or not. Defaults to true. | [optional] 

## Example

```python
from openapi_client.models.subscription_request import SubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionRequest from a JSON string
subscription_request_instance = SubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(SubscriptionRequest.to_json())

# convert the object into a dict
subscription_request_dict = subscription_request_instance.to_dict()
# create an instance of SubscriptionRequest from a dict
subscription_request_from_dict = SubscriptionRequest.from_dict(subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


