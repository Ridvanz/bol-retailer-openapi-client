# openapi_client.OrdersApi

All URIs are relative to *https://api.bol.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_order_item**](OrdersApi.md#cancel_order_item) | **PUT** /retailer/orders/cancellation | Cancel an order item by an order item id
[**get_order**](OrdersApi.md#get_order) | **GET** /retailer/orders/{order-id} | Get an order by order id
[**get_orders**](OrdersApi.md#get_orders) | **GET** /retailer/orders | Get a list of orders


# **cancel_order_item**
> ProcessStatus cancel_order_item(cancellation_request)

Cancel an order item by an order item id

This endpoint can be used to either confirm a cancellation request by the customer or to cancel an order item you yourself are unable to fulfil.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.cancellation_request import CancellationRequest
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
    api_instance = openapi_client.OrdersApi(api_client)
    cancellation_request = openapi_client.CancellationRequest() # CancellationRequest | 

    try:
        # Cancel an order item by an order item id
        api_response = api_instance.cancel_order_item(cancellation_request)
        print("The response of OrdersApi->cancel_order_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->cancel_order_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cancellation_request** | [**CancellationRequest**](CancellationRequest.md)|  | 

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

# **get_order**
> Order get_order(order_id)

Get an order by order id

Gets an order by order id. The order can be partially shipped or cancelled, and the message contains the quantity shipped or cancelled items. The unitPrice takes account of volume discounts.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.order import Order
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
    api_instance = openapi_client.OrdersApi(api_client)
    order_id = 'order_id_example' # str | The id of the order to get.

    try:
        # Get an order by order id
        api_response = api_instance.get_order(order_id)
        print("The response of OrdersApi->get_order:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_order: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order_id** | **str**| The id of the order to get. | 

### Return type

[**Order**](Order.md)

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

# **get_orders**
> ReducedOrders get_orders(page=page, fulfilment_method=fulfilment_method, status=status, change_interval_minute=change_interval_minute, latest_change_date=latest_change_date)

Get a list of orders

Gets a paginated list of all orders for a retailer.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.reduced_orders import ReducedOrders
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
    api_instance = openapi_client.OrdersApi(api_client)
    page = 1 # int | The requested page number with a page size of 50 items. (optional) (default to 1)
    fulfilment_method = 'fulfilment_method_example' # str | Fulfilled by the retailer (FBR) or fulfilled by bol.com (FBB). In order to retrieve both FBR and FBB orders, ALL can be used as a parameter. (optional)
    status = 'status_example' # str | To filter on order status. You can filter on either all orders independent from their status, open orders (excluding shipped and cancelled orders), and shipped orders. (optional)
    change_interval_minute = 56 # int | To filter on the period in minutes during which the latest change was performed on an order item. (optional)
    latest_change_date = 'latest_change_date_example' # str | To filter on the date on which the latest change was performed on an order item. Up to 3 months of history is supported. (optional)

    try:
        # Get a list of orders
        api_response = api_instance.get_orders(page=page, fulfilment_method=fulfilment_method, status=status, change_interval_minute=change_interval_minute, latest_change_date=latest_change_date)
        print("The response of OrdersApi->get_orders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrdersApi->get_orders: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The requested page number with a page size of 50 items. | [optional] [default to 1]
 **fulfilment_method** | **str**| Fulfilled by the retailer (FBR) or fulfilled by bol.com (FBB). In order to retrieve both FBR and FBB orders, ALL can be used as a parameter. | [optional] 
 **status** | **str**| To filter on order status. You can filter on either all orders independent from their status, open orders (excluding shipped and cancelled orders), and shipped orders. | [optional] 
 **change_interval_minute** | **int**| To filter on the period in minutes during which the latest change was performed on an order item. | [optional] 
 **latest_change_date** | **str**| To filter on the date on which the latest change was performed on an order item. Up to 3 months of history is supported. | [optional] 

### Return type

[**ReducedOrders**](ReducedOrders.md)

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

