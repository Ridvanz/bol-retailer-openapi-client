# openapi_client.ReplenishmentsApi

All URIs are relative to *https://api.bol.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_delivery_dates**](ReplenishmentsApi.md#get_delivery_dates) | **GET** /retailer/replenishments/delivery-dates | Get delivery dates
[**get_load_carrier_labels**](ReplenishmentsApi.md#get_load_carrier_labels) | **GET** /retailer/replenishments/{replenishment-id}/load-carrier-labels | Get load carrier labels
[**get_pick_list**](ReplenishmentsApi.md#get_pick_list) | **GET** /retailer/replenishments/{replenishment-id}/pick-list | Get pick list
[**get_product_destinations**](ReplenishmentsApi.md#get_product_destinations) | **GET** /retailer/replenishments/product-destinations/{product-destinations-id} | Get product destinations by product destinations id
[**get_replenishment**](ReplenishmentsApi.md#get_replenishment) | **GET** /retailer/replenishments/{replenishment-id} | Get a replenishment by replenishment id
[**get_replenishments**](ReplenishmentsApi.md#get_replenishments) | **GET** /retailer/replenishments | Get replenishments
[**post_pickup_time_slots**](ReplenishmentsApi.md#post_pickup_time_slots) | **POST** /retailer/replenishments/pickup-time-slots | Post pickup time slots
[**post_product_labels**](ReplenishmentsApi.md#post_product_labels) | **POST** /retailer/replenishments/product-labels | Post product labels
[**post_replenishment**](ReplenishmentsApi.md#post_replenishment) | **POST** /retailer/replenishments | Create a replenishment
[**post_request_product_destinations**](ReplenishmentsApi.md#post_request_product_destinations) | **POST** /retailer/replenishments/product-destinations | Request product destinations
[**put_replenishment**](ReplenishmentsApi.md#put_replenishment) | **PUT** /retailer/replenishments/{replenishment-id} | Update a replenishment by replenishment id


# **get_delivery_dates**
> DeliveryDatesResponse get_delivery_dates()

Get delivery dates

Retrieve a list of available delivery dates for a replenishment.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.delivery_dates_response import DeliveryDatesResponse
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
    api_instance = openapi_client.ReplenishmentsApi(api_client)

    try:
        # Get delivery dates
        api_response = api_instance.get_delivery_dates()
        print("The response of ReplenishmentsApi->get_delivery_dates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReplenishmentsApi->get_delivery_dates: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DeliveryDatesResponse**](DeliveryDatesResponse.md)

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

# **get_load_carrier_labels**
> bytearray get_load_carrier_labels(replenishment_id, label_type=label_type)

Get load carrier labels

Retrieve the load carrier labels.

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
    api_instance = openapi_client.ReplenishmentsApi(api_client)
    replenishment_id = '2312078154' # str | The unique identifier of the replenishment.
    label_type = 'WAREHOUSE' # str | The type of label which you want to print. (optional)

    try:
        # Get load carrier labels
        api_response = api_instance.get_load_carrier_labels(replenishment_id, label_type=label_type)
        print("The response of ReplenishmentsApi->get_load_carrier_labels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReplenishmentsApi->get_load_carrier_labels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replenishment_id** | **str**| The unique identifier of the replenishment. | 
 **label_type** | **str**| The type of label which you want to print. | [optional] 

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
**200** | Ok: Successfully processed the request. |  -  |
**404** | Not found: The requested item could not be found. |  -  |
**400** | Bad request: The sent request does not meet the API specification. Please check the error message(s) for more information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pick_list**
> bytearray get_pick_list(replenishment_id)

Get pick list

Retrieve the pick list.

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
    api_instance = openapi_client.ReplenishmentsApi(api_client)
    replenishment_id = '2312078154' # str | The unique identifier of the replenishment.

    try:
        # Get pick list
        api_response = api_instance.get_pick_list(replenishment_id)
        print("The response of ReplenishmentsApi->get_pick_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReplenishmentsApi->get_pick_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replenishment_id** | **str**| The unique identifier of the replenishment. | 

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
**200** | Ok: Successfully processed the request. |  -  |
**404** | Not found: The requested item could not be found. |  -  |
**400** | Bad request: The sent request does not meet the API specification. Please check the error message(s) for more information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_destinations**
> ProductDestinationsResponse get_product_destinations(product_destinations_id)

Get product destinations by product destinations id

Gets the product destinations for one or more products by product destinations id.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.product_destinations_response import ProductDestinationsResponse
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
    api_instance = openapi_client.ReplenishmentsApi(api_client)
    product_destinations_id = '9483fc7e-faf3-4814-864e-dee412044c27' # str | The identifier of the product destinations requested.

    try:
        # Get product destinations by product destinations id
        api_response = api_instance.get_product_destinations(product_destinations_id)
        print("The response of ReplenishmentsApi->get_product_destinations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReplenishmentsApi->get_product_destinations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_destinations_id** | **str**| The identifier of the product destinations requested. | 

### Return type

[**ProductDestinationsResponse**](ProductDestinationsResponse.md)

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

# **get_replenishment**
> ReplenishmentResponse get_replenishment(replenishment_id)

Get a replenishment by replenishment id

Gets a replenishment by replenishment id.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.replenishment_response import ReplenishmentResponse
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
    api_instance = openapi_client.ReplenishmentsApi(api_client)
    replenishment_id = '2312078154' # str | The unique identifier of the replenishment.

    try:
        # Get a replenishment by replenishment id
        api_response = api_instance.get_replenishment(replenishment_id)
        print("The response of ReplenishmentsApi->get_replenishment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReplenishmentsApi->get_replenishment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replenishment_id** | **str**| The unique identifier of the replenishment. | 

### Return type

[**ReplenishmentResponse**](ReplenishmentResponse.md)

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

# **get_replenishments**
> ReplenishmentsResponse get_replenishments(reference=reference, ean=ean, start_date=start_date, end_date=end_date, state=state, page=page)

Get replenishments

Gets a list of replenishments.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.replenishments_response import ReplenishmentsResponse
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
    api_instance = openapi_client.ReplenishmentsApi(api_client)
    reference = 'REFERENCE1' # str | Custom user defined reference to identify the replenishment. (optional)
    ean = '0000007740404' # str | The EAN number associated with this product. (optional)
    start_date = '2021-01-01' # str | The creation start date to find the replenishment. In ISO 8601 format. (optional)
    end_date = '2021-01-02' # str | The end date of the range to find the replenishment. In ISO 8601 format. (optional)
    state = ['ANNOUNCED'] # List[str] | The current state(s) of the replenishment. (optional)
    page = 1 # int | The requested page number with a page size of 50 items. (optional) (default to 1)

    try:
        # Get replenishments
        api_response = api_instance.get_replenishments(reference=reference, ean=ean, start_date=start_date, end_date=end_date, state=state, page=page)
        print("The response of ReplenishmentsApi->get_replenishments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReplenishmentsApi->get_replenishments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reference** | **str**| Custom user defined reference to identify the replenishment. | [optional] 
 **ean** | **str**| The EAN number associated with this product. | [optional] 
 **start_date** | **str**| The creation start date to find the replenishment. In ISO 8601 format. | [optional] 
 **end_date** | **str**| The end date of the range to find the replenishment. In ISO 8601 format. | [optional] 
 **state** | [**List[str]**](str.md)| The current state(s) of the replenishment. | [optional] 
 **page** | **int**| The requested page number with a page size of 50 items. | [optional] [default to 1]

### Return type

[**ReplenishmentsResponse**](ReplenishmentsResponse.md)

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

# **post_pickup_time_slots**
> PickupTimeSlotsResponse post_pickup_time_slots(pickup_time_slots_request)

Post pickup time slots

Retrieve pickup time slots.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.pickup_time_slots_request import PickupTimeSlotsRequest
from openapi_client.models.pickup_time_slots_response import PickupTimeSlotsResponse
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
    api_instance = openapi_client.ReplenishmentsApi(api_client)
    pickup_time_slots_request = openapi_client.PickupTimeSlotsRequest() # PickupTimeSlotsRequest | 

    try:
        # Post pickup time slots
        api_response = api_instance.post_pickup_time_slots(pickup_time_slots_request)
        print("The response of ReplenishmentsApi->post_pickup_time_slots:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReplenishmentsApi->post_pickup_time_slots: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pickup_time_slots_request** | [**PickupTimeSlotsRequest**](PickupTimeSlotsRequest.md)|  | 

### Return type

[**PickupTimeSlotsResponse**](PickupTimeSlotsResponse.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_product_labels**
> bytearray post_product_labels(product_labels_request)

Post product labels

Retrieve product labels.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.product_labels_request import ProductLabelsRequest
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
    api_instance = openapi_client.ReplenishmentsApi(api_client)
    product_labels_request = openapi_client.ProductLabelsRequest() # ProductLabelsRequest | 

    try:
        # Post product labels
        api_response = api_instance.post_product_labels(product_labels_request)
        print("The response of ReplenishmentsApi->post_product_labels:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReplenishmentsApi->post_product_labels: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_labels_request** | [**ProductLabelsRequest**](ProductLabelsRequest.md)|  | 

### Return type

**bytearray**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/vnd.retailer.v10+json
 - **Accept**: application/vnd.retailer.v10+pdf

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok: Successfully processed the request. |  -  |
**404** | Not found: The requested item could not be found. |  -  |
**400** | Bad request: The sent request does not meet the API specification. Please check the error message(s) for more information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_replenishment**
> ProcessStatus post_replenishment(create_replenishment_request)

Create a replenishment

Creates a replenishment.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.create_replenishment_request import CreateReplenishmentRequest
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
    api_instance = openapi_client.ReplenishmentsApi(api_client)
    create_replenishment_request = openapi_client.CreateReplenishmentRequest() # CreateReplenishmentRequest | 

    try:
        # Create a replenishment
        api_response = api_instance.post_replenishment(create_replenishment_request)
        print("The response of ReplenishmentsApi->post_replenishment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReplenishmentsApi->post_replenishment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_replenishment_request** | [**CreateReplenishmentRequest**](CreateReplenishmentRequest.md)|  | 

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

# **post_request_product_destinations**
> ProcessStatus post_request_product_destinations(request_product_destinations_request)

Request product destinations

Requests a list of product destinations by EANs.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.process_status import ProcessStatus
from openapi_client.models.request_product_destinations_request import RequestProductDestinationsRequest
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
    api_instance = openapi_client.ReplenishmentsApi(api_client)
    request_product_destinations_request = openapi_client.RequestProductDestinationsRequest() # RequestProductDestinationsRequest | 

    try:
        # Request product destinations
        api_response = api_instance.post_request_product_destinations(request_product_destinations_request)
        print("The response of ReplenishmentsApi->post_request_product_destinations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReplenishmentsApi->post_request_product_destinations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_product_destinations_request** | [**RequestProductDestinationsRequest**](RequestProductDestinationsRequest.md)|  | 

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

# **put_replenishment**
> ProcessStatus put_replenishment(replenishment_id, update_replenishment_request)

Update a replenishment by replenishment id

Updates a replenishment.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.process_status import ProcessStatus
from openapi_client.models.update_replenishment_request import UpdateReplenishmentRequest
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
    api_instance = openapi_client.ReplenishmentsApi(api_client)
    replenishment_id = '2312078154' # str | The unique identifier of the replenishment.
    update_replenishment_request = openapi_client.UpdateReplenishmentRequest() # UpdateReplenishmentRequest | 

    try:
        # Update a replenishment by replenishment id
        api_response = api_instance.put_replenishment(replenishment_id, update_replenishment_request)
        print("The response of ReplenishmentsApi->put_replenishment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReplenishmentsApi->put_replenishment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **replenishment_id** | **str**| The unique identifier of the replenishment. | 
 **update_replenishment_request** | [**UpdateReplenishmentRequest**](UpdateReplenishmentRequest.md)|  | 

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

