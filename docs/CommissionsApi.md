# openapi_client.CommissionsApi

All URIs are relative to *https://api.bol.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_commission**](CommissionsApi.md#get_commission) | **GET** /retailer/commission/{ean} | Get all commissions and reductions by EAN per single EAN
[**get_commission_rates**](CommissionsApi.md#get_commission_rates) | **POST** /retailer/commissions | Get a list of commissions by EAN (BETA)
[**get_commissions**](CommissionsApi.md#get_commissions) | **POST** /retailer/commission | Get all commissions and reductions by EAN in bulk


# **get_commission**
> Commission get_commission(ean, unit_price, condition=condition)

Get all commissions and reductions by EAN per single EAN

Commissions can be filtered by condition, which defaults to NEW. We will calculate the commission amount from the EAN and price.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.commission import Commission
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
    api_instance = openapi_client.CommissionsApi(api_client)
    ean = '0000007740404' # str | The EAN number associated with this product.
    unit_price = 59.0 # float | The price of the product with a period as a decimal separator. The price should always have two decimals precision.
    condition = 'condition_example' # str | The condition of the offer. (optional)

    try:
        # Get all commissions and reductions by EAN per single EAN
        api_response = api_instance.get_commission(ean, unit_price, condition=condition)
        print("The response of CommissionsApi->get_commission:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommissionsApi->get_commission: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ean** | **str**| The EAN number associated with this product. | 
 **unit_price** | **float**| The price of the product with a period as a decimal separator. The price should always have two decimals precision. | 
 **condition** | **str**| The condition of the offer. | [optional] 

### Return type

[**Commission**](Commission.md)

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

# **get_commission_rates**
> BulkCommissionRatesMultiStatusResponse get_commission_rates(commission_products)

Get a list of commissions by EAN (BETA)

Gets a list of all commissions using EAN.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.bulk_commission_rates_multi_status_response import BulkCommissionRatesMultiStatusResponse
from openapi_client.models.commission_products import CommissionProducts
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
    api_instance = openapi_client.CommissionsApi(api_client)
    commission_products = openapi_client.CommissionProducts() # CommissionProducts | 

    try:
        # Get a list of commissions by EAN (BETA)
        api_response = api_instance.get_commission_rates(commission_products)
        print("The response of CommissionsApi->get_commission_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommissionsApi->get_commission_rates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **commission_products** | [**CommissionProducts**](CommissionProducts.md)|  | 

### Return type

[**BulkCommissionRatesMultiStatusResponse**](BulkCommissionRatesMultiStatusResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/vnd.retailer.v10+json
 - **Accept**: application/vnd.retailer.v10+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**207** | Multi-status: Retrieved successful and unsuccessful results. |  -  |
**400** | Bad request: The sent request does not meet the API specification. Please check the error message(s) for more information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_commissions**
> BulkCommissionResponse get_commissions(bulk_commission_request)

Get all commissions and reductions by EAN in bulk

Gets all commissions and possible reductions by EAN, price, and optionally condition.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.bulk_commission_request import BulkCommissionRequest
from openapi_client.models.bulk_commission_response import BulkCommissionResponse
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
    api_instance = openapi_client.CommissionsApi(api_client)
    bulk_commission_request = openapi_client.BulkCommissionRequest() # BulkCommissionRequest | 

    try:
        # Get all commissions and reductions by EAN in bulk
        api_response = api_instance.get_commissions(bulk_commission_request)
        print("The response of CommissionsApi->get_commissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommissionsApi->get_commissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_commission_request** | [**BulkCommissionRequest**](BulkCommissionRequest.md)|  | 

### Return type

[**BulkCommissionResponse**](BulkCommissionResponse.md)

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

