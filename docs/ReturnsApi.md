# openapi_client.ReturnsApi

All URIs are relative to *https://api.bol.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_return**](ReturnsApi.md#create_return) | **POST** /retailer/returns | Create a return
[**get_return**](ReturnsApi.md#get_return) | **GET** /retailer/returns/{return-id} | Get a return by return id
[**get_returns**](ReturnsApi.md#get_returns) | **GET** /retailer/returns | Get returns
[**handle_return**](ReturnsApi.md#handle_return) | **PUT** /retailer/returns/{rma-id} | Handle a return by rma id


# **create_return**
> ProcessStatus create_return(create_return_request)

Create a return

Create a return, and automatically handle it with the provided handling result. When successfully created, the resulting return id is provided in the process status.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.create_return_request import CreateReturnRequest
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
    api_instance = openapi_client.ReturnsApi(api_client)
    create_return_request = openapi_client.CreateReturnRequest() # CreateReturnRequest | 

    try:
        # Create a return
        api_response = api_instance.create_return(create_return_request)
        print("The response of ReturnsApi->create_return:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnsApi->create_return: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_return_request** | [**CreateReturnRequest**](CreateReturnRequest.md)|  | 

### Return type

[**ProcessStatus**](ProcessStatus.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.retailer.v10+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted: Successfully scheduled the request for processing. |  -  |
**400** | Bad request: The sent request does not meet the API specification. Please check the error message(s) for more information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_return**
> ModelReturn get_return(return_id)

Get a return by return id

Retrieve a return based on the return id.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.model_return import ModelReturn
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
    api_instance = openapi_client.ReturnsApi(api_client)
    return_id = 'return_id_example' # str | Unique identifier for a return.

    try:
        # Get a return by return id
        api_response = api_instance.get_return(return_id)
        print("The response of ReturnsApi->get_return:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnsApi->get_return: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_id** | **str**| Unique identifier for a return. | 

### Return type

[**ModelReturn**](ModelReturn.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_returns**
> ReturnsResponse get_returns(page=page, handled=handled, fulfilment_method=fulfilment_method)

Get returns

Get a paginated list of multi-item returns. Handled returns are sorted by date in descending order, while unhandled returns are sorted by date in ascending order.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.returns_response import ReturnsResponse
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
    api_instance = openapi_client.ReturnsApi(api_client)
    page = 1 # int | The page to get with a page size of 50. (optional) (default to 1)
    handled = True # bool | The status of the returns you wish to see, shows either handled or unhandled returns. (optional)
    fulfilment_method = 'fulfilment_method_example' # str | The fulfilment method. Fulfilled by the retailer (FBR) or fulfilled by bol.com (FBB). (optional)

    try:
        # Get returns
        api_response = api_instance.get_returns(page=page, handled=handled, fulfilment_method=fulfilment_method)
        print("The response of ReturnsApi->get_returns:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnsApi->get_returns: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page to get with a page size of 50. | [optional] [default to 1]
 **handled** | **bool**| The status of the returns you wish to see, shows either handled or unhandled returns. | [optional] 
 **fulfilment_method** | **str**| The fulfilment method. Fulfilled by the retailer (FBR) or fulfilled by bol.com (FBB). | [optional] 

### Return type

[**ReturnsResponse**](ReturnsResponse.md)

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

# **handle_return**
> ProcessStatus handle_return(rma_id, return_request)

Handle a return by rma id

Allows the user to handle a return. This can be to either handle an open return, or change the handlingResult of an already handled return. Please refer to the Returns documentation for further details.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.process_status import ProcessStatus
from openapi_client.models.return_request import ReturnRequest
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
    api_instance = openapi_client.ReturnsApi(api_client)
    rma_id = 56 # int | The RMA (Return Merchandise Authorization) identifier of the return.
    return_request = openapi_client.ReturnRequest() # ReturnRequest | 

    try:
        # Handle a return by rma id
        api_response = api_instance.handle_return(rma_id, return_request)
        print("The response of ReturnsApi->handle_return:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReturnsApi->handle_return: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rma_id** | **int**| The RMA (Return Merchandise Authorization) identifier of the return. | 
 **return_request** | [**ReturnRequest**](ReturnRequest.md)|  | 

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

