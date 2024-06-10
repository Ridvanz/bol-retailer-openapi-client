# openapi_client.InvoicesApi

All URIs are relative to *https://api.bol.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_invoice**](InvoicesApi.md#get_invoice) | **GET** /retailer/invoices/{invoice-id} | Get an invoice by invoice id
[**get_invoice_specification**](InvoicesApi.md#get_invoice_specification) | **GET** /retailer/invoices/{invoice-id}/specification | Get an invoice specification by invoice id
[**get_invoices**](InvoicesApi.md#get_invoices) | **GET** /retailer/invoices | Get all invoices


# **get_invoice**
> bytearray get_invoice(invoice_id)

Get an invoice by invoice id

Gets an invoice by invoice id. The available media types differ per invoice and are listed within the response from the ‘GET all invoices’ call. Note: the media types listed in the response must be given in our standard API format.

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
    api_instance = openapi_client.InvoicesApi(api_client)
    invoice_id = 'invoice_id_example' # str | The id of the invoice

    try:
        # Get an invoice by invoice id
        api_response = api_instance.get_invoice(invoice_id)
        print("The response of InvoicesApi->get_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->get_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**| The id of the invoice | 

### Return type

**bytearray**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.retailer.v10+json, application/vnd.retailer.v10+pdf

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok: Successfully processed the request. |  -  |
**400** | Bad request: The sent request does not meet the API specification. Please check the error message(s) for more information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoice_specification**
> bytearray get_invoice_specification(invoice_id, page=page)

Get an invoice specification by invoice id

Gets an invoice specification for an invoice with a paginated list of its transactions. The available media types differ per invoice specification and are listed within the response from the ‘GET all invoices’ call. Note, the media types listed in the response must be given in our standard API format.

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
    api_instance = openapi_client.InvoicesApi(api_client)
    invoice_id = 'invoice_id_example' # str | The identifier of the invoice.
    page = 56 # int | The requested page number with a maximum of 25,000 lines. (optional)

    try:
        # Get an invoice specification by invoice id
        api_response = api_instance.get_invoice_specification(invoice_id, page=page)
        print("The response of InvoicesApi->get_invoice_specification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->get_invoice_specification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invoice_id** | **str**| The identifier of the invoice. | 
 **page** | **int**| The requested page number with a maximum of 25,000 lines. | [optional] 

### Return type

**bytearray**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.retailer.v10+json, application/vnd.retailer.v10+openxmlformats-officedocument.spreadsheetml.sheet

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok: Successfully processed the request. |  -  |
**400** | Bad request: The sent request does not meet the API specification. Please check the error message(s) for more information. |  -  |
**404** | Not found: The requested item could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invoices**
> bytearray get_invoices(period_start_date=period_start_date, period_end_date=period_end_date)

Get all invoices

Gets a list of invoices, by default from the past 4 weeks. The optional period-start-date and period-end-date-date parameters can be used together to retrieve invoices from a specific date range in the past, the period can be no longer than 31 days. Invoices and their specifications can be downloaded separately in different media formats with the ‘GET an invoice by id’ and the ‘GET an invoice specification by id’ calls. The available media types differ per invoice and are listed per invoice within the response. Note: the media types listed in the response must be given in our standard API format.

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
    api_instance = openapi_client.InvoicesApi(api_client)
    period_start_date = '2019-03-01' # str | Period start date in ISO 8601 standard. (optional)
    period_end_date = '2019-03-31' # str | Period end date in ISO 8601 standard. (optional)

    try:
        # Get all invoices
        api_response = api_instance.get_invoices(period_start_date=period_start_date, period_end_date=period_end_date)
        print("The response of InvoicesApi->get_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InvoicesApi->get_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **period_start_date** | **str**| Period start date in ISO 8601 standard. | [optional] 
 **period_end_date** | **str**| Period end date in ISO 8601 standard. | [optional] 

### Return type

**bytearray**

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

