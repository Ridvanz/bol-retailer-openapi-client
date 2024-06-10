# openapi_client.TransportsApi

All URIs are relative to *https://api.bol.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_transport_information_by_transport_id**](TransportsApi.md#add_transport_information_by_transport_id) | **PUT** /retailer/transports/{transport-id} | Add transport information by transport id


# **add_transport_information_by_transport_id**
> ProcessStatus add_transport_information_by_transport_id(transport_id, change_transport_request)

Add transport information by transport id

Add information to an existing transport. The transport id is part of the shipment. You can retrieve the transport id through the GET shipment list request.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.change_transport_request import ChangeTransportRequest
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
    api_instance = openapi_client.TransportsApi(api_client)
    transport_id = 'transport_id_example' # str | The transport id.
    change_transport_request = openapi_client.ChangeTransportRequest() # ChangeTransportRequest | 

    try:
        # Add transport information by transport id
        api_response = api_instance.add_transport_information_by_transport_id(transport_id, change_transport_request)
        print("The response of TransportsApi->add_transport_information_by_transport_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TransportsApi->add_transport_information_by_transport_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transport_id** | **str**| The transport id. | 
 **change_transport_request** | [**ChangeTransportRequest**](ChangeTransportRequest.md)|  | 

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

