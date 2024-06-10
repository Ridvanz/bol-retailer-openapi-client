# openapi_client.ShipmentsApi

All URIs are relative to *https://api.bol.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_shipment**](ShipmentsApi.md#create_shipment) | **POST** /retailer/shipments | Create a shipment
[**get_invoice_requests**](ShipmentsApi.md#get_invoice_requests) | **GET** /retailer/shipments/invoices/requests | Get a list of invoice requests
[**get_shipment**](ShipmentsApi.md#get_shipment) | **GET** /retailer/shipments/{shipment-id} | Get a shipment by shipment id
[**get_shipments**](ShipmentsApi.md#get_shipments) | **GET** /retailer/shipments | Get shipment list
[**upload_invoice**](ShipmentsApi.md#upload_invoice) | **POST** /retailer/shipments/invoices/{shipment-id} | Upload an invoice for shipment id


# **create_shipment**
> ProcessStatus create_shipment(shipment_request)

Create a shipment

Ship multiple single order items within a customer order by providing shipping information. If you purchased a shipping label you should add the shippingLabelId to this message and leave the transport element empty. If you will ship the item using your own transporter method you must omit the shippingLabelId entirely and fill in the transport element with the fields from GET shipping labels.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.process_status import ProcessStatus
from openapi_client.models.shipment_request import ShipmentRequest
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
    api_instance = openapi_client.ShipmentsApi(api_client)
    shipment_request = openapi_client.ShipmentRequest() # ShipmentRequest | 

    try:
        # Create a shipment
        api_response = api_instance.create_shipment(shipment_request)
        print("The response of ShipmentsApi->create_shipment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentsApi->create_shipment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_request** | [**ShipmentRequest**](ShipmentRequest.md)|  | 

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

# **get_invoice_requests**
> InvoiceRequestsResponse get_invoice_requests(shipment_id=shipment_id, page=page, state=state)

Get a list of invoice requests

Gets a list of paginated invoice requests initiated by customers.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.invoice_requests_response import InvoiceRequestsResponse
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
    api_instance = openapi_client.ShipmentsApi(api_client)
    shipment_id = '541757635' # str | The id of the shipment. (optional)
    page = 1 # int | The requested page number with a page size of 50 items. (optional) (default to 1)
    state = 'OPEN' # str | To filter on invoice request state. You can filter on all invoice requests regardless their statuses, open invoice requests requiring your action and invoice requests uploaded with possible errors. (optional)

    try:
        # Get a list of invoice requests
        api_response = api_instance.get_invoice_requests(shipment_id=shipment_id, page=page, state=state)
        print("The response of ShipmentsApi->get_invoice_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentsApi->get_invoice_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| The id of the shipment. | [optional] 
 **page** | **int**| The requested page number with a page size of 50 items. | [optional] [default to 1]
 **state** | **str**| To filter on invoice request state. You can filter on all invoice requests regardless their statuses, open invoice requests requiring your action and invoice requests uploaded with possible errors. | [optional] 

### Return type

[**InvoiceRequestsResponse**](InvoiceRequestsResponse.md)

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

# **get_shipment**
> Shipment get_shipment(shipment_id)

Get a shipment by shipment id

Retrieve a single shipment by its corresponding id.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.shipment import Shipment
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
    api_instance = openapi_client.ShipmentsApi(api_client)
    shipment_id = 'shipment_id_example' # str | The id of the shipment.

    try:
        # Get a shipment by shipment id
        api_response = api_instance.get_shipment(shipment_id)
        print("The response of ShipmentsApi->get_shipment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentsApi->get_shipment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| The id of the shipment. | 

### Return type

[**Shipment**](Shipment.md)

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

# **get_shipments**
> ShipmentsResponse get_shipments(page=page, fulfilment_method=fulfilment_method, order_id=order_id)

Get shipment list

A paginated list to retrieve all your shipments up to 3 months old. The shipments will be sorted by date in descending order.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.shipments_response import ShipmentsResponse
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
    api_instance = openapi_client.ShipmentsApi(api_client)
    page = 1 # int | The page to get with a page size of 50. (optional) (default to 1)
    fulfilment_method = 'fulfilment_method_example' # str | The fulfilment method. Fulfilled by the retailer (FBR) or fulfilled by bol.com (FBB). (optional)
    order_id = 'order_id_example' # str | The id of the order. Only valid without fulfilment-method. The default fulfilment-method is ignored. (optional)

    try:
        # Get shipment list
        api_response = api_instance.get_shipments(page=page, fulfilment_method=fulfilment_method, order_id=order_id)
        print("The response of ShipmentsApi->get_shipments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentsApi->get_shipments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The page to get with a page size of 50. | [optional] [default to 1]
 **fulfilment_method** | **str**| The fulfilment method. Fulfilled by the retailer (FBR) or fulfilled by bol.com (FBB). | [optional] 
 **order_id** | **str**| The id of the order. Only valid without fulfilment-method. The default fulfilment-method is ignored. | [optional] 

### Return type

[**ShipmentsResponse**](ShipmentsResponse.md)

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

# **upload_invoice**
> ProcessStatus upload_invoice(shipment_id, upload_invoice_request)

Upload an invoice for shipment id

Uploads an invoice associated with shipment id.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.process_status import ProcessStatus
from openapi_client.models.upload_invoice_request import UploadInvoiceRequest
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
    api_instance = openapi_client.ShipmentsApi(api_client)
    shipment_id = '541757635' # str | The id of the shipment associated with the invoice.
    upload_invoice_request = openapi_client.UploadInvoiceRequest() # UploadInvoiceRequest | 

    try:
        # Upload an invoice for shipment id
        api_response = api_instance.upload_invoice(shipment_id, upload_invoice_request)
        print("The response of ShipmentsApi->upload_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ShipmentsApi->upload_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shipment_id** | **str**| The id of the shipment associated with the invoice. | 
 **upload_invoice_request** | [**UploadInvoiceRequest**](UploadInvoiceRequest.md)|  | 

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
**404** | Not found: The requested item could not be found. |  -  |
**415** | Unsupported Media Type: Content-Type header contains invalid value, allowed value is multipart/form-data. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

