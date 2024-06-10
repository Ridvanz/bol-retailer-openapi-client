# openapi_client.RetailersApi

All URIs are relative to *https://api.bol.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_retailer_information**](RetailersApi.md#get_retailer_information) | **GET** /retailer/retailers/{retailer-id} | Get retailer information by retailer id


# **get_retailer_information**
> RetailerInformationResponse get_retailer_information(retailer_id)

Get retailer information by retailer id

Gets retailer information of a single retailer.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.retailer_information_response import RetailerInformationResponse
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
    api_instance = openapi_client.RetailersApi(api_client)
    retailer_id = '1055479' # str | The Id of the retailer which information belongs to.

    try:
        # Get retailer information by retailer id
        api_response = api_instance.get_retailer_information(retailer_id)
        print("The response of RetailersApi->get_retailer_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RetailersApi->get_retailer_information: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **retailer_id** | **str**| The Id of the retailer which information belongs to. | 

### Return type

[**RetailerInformationResponse**](RetailerInformationResponse.md)

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
**404** | Not found: The requested item could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

