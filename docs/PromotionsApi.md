# openapi_client.PromotionsApi

All URIs are relative to *https://api.bol.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_products**](PromotionsApi.md#get_products) | **GET** /retailer/promotions/{promotion-id}/products | Get a list of products
[**get_promotion**](PromotionsApi.md#get_promotion) | **GET** /retailer/promotions/{promotion-id} | Get a promotion by promotion id
[**get_promotions**](PromotionsApi.md#get_promotions) | **GET** /retailer/promotions | Get a list of promotions


# **get_products**
> Products get_products(promotion_id, page=page)

Get a list of products

Gets a paginated list of all products that are present within a promotion.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.products import Products
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
    api_instance = openapi_client.PromotionsApi(api_client)
    promotion_id = 'promotion_id_example' # str | The identifier of the promotion.
    page = 1 # int | The requested page number with a page size of 50 items. (optional) (default to 1)

    try:
        # Get a list of products
        api_response = api_instance.get_products(promotion_id, page=page)
        print("The response of PromotionsApi->get_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionsApi->get_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **promotion_id** | **str**| The identifier of the promotion. | 
 **page** | **int**| The requested page number with a page size of 50 items. | [optional] [default to 1]

### Return type

[**Products**](Products.md)

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

# **get_promotion**
> Promotion get_promotion(promotion_id)

Get a promotion by promotion id

Gets the details of a promotion.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.promotion import Promotion
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
    api_instance = openapi_client.PromotionsApi(api_client)
    promotion_id = 'promotion_id_example' # str | The identifier of the promotion.

    try:
        # Get a promotion by promotion id
        api_response = api_instance.get_promotion(promotion_id)
        print("The response of PromotionsApi->get_promotion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionsApi->get_promotion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **promotion_id** | **str**| The identifier of the promotion. | 

### Return type

[**Promotion**](Promotion.md)

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

# **get_promotions**
> Promotions get_promotions(promotion_type, page=page)

Get a list of promotions

Gets a paginated list of all promotions for a retailer.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.promotions import Promotions
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
    api_instance = openapi_client.PromotionsApi(api_client)
    promotion_type = 'promotion_type_example' # str | The type(s) of promotion to be retrieved.
    page = 1 # int | The requested page number with a page size of 50 items. (optional) (default to 1)

    try:
        # Get a list of promotions
        api_response = api_instance.get_promotions(promotion_type, page=page)
        print("The response of PromotionsApi->get_promotions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromotionsApi->get_promotions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **promotion_type** | **str**| The type(s) of promotion to be retrieved. | 
 **page** | **int**| The requested page number with a page size of 50 items. | [optional] [default to 1]

### Return type

[**Promotions**](Promotions.md)

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

