# openapi_client.ShippingLabelsApi

All URIs are relative to *https://api.bol.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_delivery_options**](ShippingLabelsApi.md#get_delivery_options) | **POST** /retailer/shipping-labels/delivery-options | Get delivery options
[**get_shipping_label**](ShippingLabelsApi.md#get_shipping_label) | **GET** /retailer/shipping-labels/{shipping-label-id} | Get a shipping label
[**post_shipping_label**](ShippingLabelsApi.md#post_shipping_label) | **POST** /retailer/shipping-labels | Create a shipping label


# **get_delivery_options**
> DeliveryOptionsResponse get_delivery_options(delivery_options_request)

Get delivery options

Retrieves all available delivery options based on the supplied configuration of order items that has to be shipped.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.delivery_options_request import DeliveryOptionsRequest
from openapi_client.models.delivery_options_response import DeliveryOptionsResponse
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
    api_instance = openapi_client.ShippingLabelsApi(api_client)
    delivery_options_request = openapi_client.DeliveryOptionsRequest() # DeliveryOptionsRequest | 

    try:
        # Get delivery options
        api_response = api_instance.get_delivery_options(delivery_options_request)
        print("The response of ShippingLabelsApi->get_delivery_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingLabelsApi->get_delivery_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **delivery_options_request** | [**DeliveryOptionsRequest**](DeliveryOptionsRequest.md)|  | 

### Return type

[**DeliveryOptionsResponse**](DeliveryOptionsResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/vnd.retailer.v10+json
 - **Accept**: application/vnd.retailer.v10+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok: Successfully processed the request. |  -  |
**400** | Bad request: The sent request does not meet the API specification. Please check the error message(s) for more information. |  -  |
**404** | Not found: The requested item could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shipping_label**
> bytearray get_shipping_label(shipping_label_id)

Get a shipping label

Retrieves a shipping label by shipping label id. Metadata for the shipping label is added as headers in the response. If you are only interested in the metadata, you can do a HEAD request to retrieve only the headers without the label data.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
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
    api_instance = openapi_client.ShippingLabelsApi(api_client)
    shipping_label_id = '6ff736b5-cdd0-4150-8c67-78269ee986f5' # str | The shipping label id.

    try:
        # Get a shipping label
        api_response = api_instance.get_shipping_label(shipping_label_id)
        print("The response of ShippingLabelsApi->get_shipping_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingLabelsApi->get_shipping_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_label_id** | **str**| The shipping label id. | 

### Return type

**bytearray**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.retailer.v10+pdf

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok: Successfully processed the request. |  * X-Track-And-Trace-Code - Track and trace code for the retrieved label. <br>  * X-Transporter-Code - Transporter code for the retrieved label. <br>  |
**400** | Bad request: The sent request does not meet the API specification. Please check the error message(s) for more information. |  -  |
**404** | Not found: The requested item could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_shipping_label**
> ProcessStatus post_shipping_label(shipping_label_request)

Create a shipping label

Create a shipping label with a shipping label offer id retrieved from get delivery options.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.process_status import ProcessStatus
from openapi_client.models.shipping_label_request import ShippingLabelRequest
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
    api_instance = openapi_client.ShippingLabelsApi(api_client)
    shipping_label_request = openapi_client.ShippingLabelRequest() # ShippingLabelRequest | 

    try:
        # Create a shipping label
        api_response = api_instance.post_shipping_label(shipping_label_request)
        print("The response of ShippingLabelsApi->post_shipping_label:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShippingLabelsApi->post_shipping_label: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipping_label_request** | [**ShippingLabelRequest**](ShippingLabelRequest.md)|  | 

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

