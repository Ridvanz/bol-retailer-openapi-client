# openapi_client.SubscriptionsApi

All URIs are relative to *https://api.bol.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_push_notification_subscription**](SubscriptionsApi.md#delete_push_notification_subscription) | **DELETE** /retailer/subscriptions/{subscription-id} | Remove Event Notification Subscription
[**get_push_notification_subscription**](SubscriptionsApi.md#get_push_notification_subscription) | **GET** /retailer/subscriptions/{subscription-id} | Retrieve Specific Event Notification Subscription (BETA)
[**get_push_notification_subscriptions**](SubscriptionsApi.md#get_push_notification_subscriptions) | **GET** /retailer/subscriptions | Retrieve Event Notification Subscriptions (BETA)
[**get_subscription_keys**](SubscriptionsApi.md#get_subscription_keys) | **GET** /retailer/subscriptions/signature-keys | Retrieve public keys for push notification signature validation.
[**post_push_notification_subscription**](SubscriptionsApi.md#post_push_notification_subscription) | **POST** /retailer/subscriptions | Create Event Notification Subscription (BETA)
[**post_test_push_notification**](SubscriptionsApi.md#post_test_push_notification) | **POST** /retailer/subscriptions/test/{subscription-id} | Send test push notification for subscriptions
[**put_push_notification_subscription**](SubscriptionsApi.md#put_push_notification_subscription) | **PUT** /retailer/subscriptions/{subscription-id} | Update Event Notification Subscription (BETA)


# **delete_push_notification_subscription**
> ProcessStatus delete_push_notification_subscription(subscription_id)

Remove Event Notification Subscription

Deletes a specific event notification subscription associated with a retailer.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.process_status import ProcessStatus
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.bol.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.bol.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: OAuth2
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SubscriptionsApi(api_client)
    subscription_id = '1234' # str | The unique identifier assigned to each event notification subscription. This ID is used for tracking and managing each subscription.

    try:
        # Remove Event Notification Subscription
        api_response = api_instance.delete_push_notification_subscription(subscription_id)
        print("The response of SubscriptionsApi->delete_push_notification_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->delete_push_notification_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| The unique identifier assigned to each event notification subscription. This ID is used for tracking and managing each subscription. | 

### Return type

[**ProcessStatus**](ProcessStatus.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.retailer.v10+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted: Successfully scheduled the request for processing. |  -  |
**400** | Bad request: The sent request does not meet the API specification. Please check the error message(s) for more information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_push_notification_subscription**
> SubscriptionResponse get_push_notification_subscription(subscription_id)

Retrieve Specific Event Notification Subscription (BETA)

Fetches the details of a specific event notification subscription for a retailer. The details include the types of events and the destination, which can either be a URL (for WEBHOOK) or a topic name (for GCP_PUBSUB).

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.subscription_response import SubscriptionResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.bol.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.bol.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: OAuth2
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SubscriptionsApi(api_client)
    subscription_id = '1234' # str | The unique identifier assigned to each event notification subscription. This ID is used for tracking and managing each subscription.

    try:
        # Retrieve Specific Event Notification Subscription (BETA)
        api_response = api_instance.get_push_notification_subscription(subscription_id)
        print("The response of SubscriptionsApi->get_push_notification_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->get_push_notification_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| The unique identifier assigned to each event notification subscription. This ID is used for tracking and managing each subscription. | 

### Return type

[**SubscriptionResponse**](SubscriptionResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.retailer.v10+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok: Successfully processed the request. |  -  |
**404** | Not found: The requested item could not be found. |  -  |
**400** | Bad request: The sent request does not meet the API specification. Please check the error message(s) for more information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_push_notification_subscriptions**
> SubscriptionsResponse get_push_notification_subscriptions()

Retrieve Event Notification Subscriptions (BETA)

Retrieves all event notification subscriptions for a given retailer. Each subscription may have different types of events and a destination, which could either be a URL (for WEBHOOK) or a topic name (for GCP_PUBSUB).

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.subscriptions_response import SubscriptionsResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.bol.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.bol.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: OAuth2
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SubscriptionsApi(api_client)

    try:
        # Retrieve Event Notification Subscriptions (BETA)
        api_response = api_instance.get_push_notification_subscriptions()
        print("The response of SubscriptionsApi->get_push_notification_subscriptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->get_push_notification_subscriptions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SubscriptionsResponse**](SubscriptionsResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.retailer.v10+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok: Successfully processed the request. |  -  |
**400** | Bad request: The sent request does not meet the API specification. Please check the error message(s) for more information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_keys**
> KeySetResponse get_subscription_keys()

Retrieve public keys for push notification signature validation.

Retrieve a list of public keys that should be used to validate the signature header for push notifications received from bol.com.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.key_set_response import KeySetResponse
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.bol.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.bol.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: OAuth2
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SubscriptionsApi(api_client)

    try:
        # Retrieve public keys for push notification signature validation.
        api_response = api_instance.get_subscription_keys()
        print("The response of SubscriptionsApi->get_subscription_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->get_subscription_keys: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**KeySetResponse**](KeySetResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.retailer.v10+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok: Successfully processed the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_push_notification_subscription**
> ProcessStatus post_push_notification_subscription(subscription_request)

Create Event Notification Subscription (BETA)

Creates a new event notification subscription for a retailer. The subscription can be set up for one or more types of events and the destination can either be a URL (for WEBHOOK) or a topic name (for GCP_PUBSUB).

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.process_status import ProcessStatus
from openapi_client.models.subscription_request import SubscriptionRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.bol.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.bol.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: OAuth2
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SubscriptionsApi(api_client)
    subscription_request = openapi_client.SubscriptionRequest() # SubscriptionRequest | 

    try:
        # Create Event Notification Subscription (BETA)
        api_response = api_instance.post_push_notification_subscription(subscription_request)
        print("The response of SubscriptionsApi->post_push_notification_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->post_push_notification_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_request** | [**SubscriptionRequest**](SubscriptionRequest.md)|  | 

### Return type

[**ProcessStatus**](ProcessStatus.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/vnd.retailer.v10+json
 - **Accept**: application/vnd.retailer.v10+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted: Successfully scheduled the request for processing. |  -  |
**400** | Bad request: The sent request does not meet the API specification. Please check the error message(s) for more information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_test_push_notification**
> ProcessStatus post_test_push_notification(subscription_id)

Send test push notification for subscriptions

Send a test push notification to all subscriptions for the provided event.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.process_status import ProcessStatus
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.bol.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.bol.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: OAuth2
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SubscriptionsApi(api_client)
    subscription_id = '1234' # str | The unique identifier assigned to each event notification subscription. This ID is used for tracking and managing each subscription.

    try:
        # Send test push notification for subscriptions
        api_response = api_instance.post_test_push_notification(subscription_id)
        print("The response of SubscriptionsApi->post_test_push_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->post_test_push_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| The unique identifier assigned to each event notification subscription. This ID is used for tracking and managing each subscription. | 

### Return type

[**ProcessStatus**](ProcessStatus.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.retailer.v10+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted: Successfully scheduled the request for processing. |  -  |
**400** | Bad request: The sent request does not meet the API specification. Please check the error message(s) for more information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_push_notification_subscription**
> ProcessStatus put_push_notification_subscription(subscription_id, subscription_request)

Update Event Notification Subscription (BETA)

Updates the details of a specific event notification subscription for a retailer. The updates can be made to the types of events and/or the destination, which can either be a URL (for WEBHOOK) or a topic name (for GCP_PUBSUB).

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.process_status import ProcessStatus
from openapi_client.models.subscription_request import SubscriptionRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.bol.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.bol.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: OAuth2
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.SubscriptionsApi(api_client)
    subscription_id = '1234' # str | The unique identifier assigned to each event notification subscription. This ID is used for tracking and managing each subscription.
    subscription_request = openapi_client.SubscriptionRequest() # SubscriptionRequest | 

    try:
        # Update Event Notification Subscription (BETA)
        api_response = api_instance.put_push_notification_subscription(subscription_id, subscription_request)
        print("The response of SubscriptionsApi->put_push_notification_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SubscriptionsApi->put_push_notification_subscription: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **subscription_id** | **str**| The unique identifier assigned to each event notification subscription. This ID is used for tracking and managing each subscription. | 
 **subscription_request** | [**SubscriptionRequest**](SubscriptionRequest.md)|  | 

### Return type

[**ProcessStatus**](ProcessStatus.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/vnd.retailer.v10+json
 - **Accept**: application/vnd.retailer.v10+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted: Successfully scheduled the request for processing. |  -  |
**400** | Bad request: The sent request does not meet the API specification. Please check the error message(s) for more information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

