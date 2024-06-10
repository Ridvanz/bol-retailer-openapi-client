# openapi_client.ProductsApi

All URIs are relative to *https://api.bol.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_competing_offers**](ProductsApi.md#get_competing_offers) | **GET** /retailer/products/{ean}/offers | Get a list of competing offers by EAN
[**get_price_star_boundaries**](ProductsApi.md#get_price_star_boundaries) | **GET** /retailer/products/{ean}/price-star-boundaries | Get price star boundaries by EAN
[**get_product_assets**](ProductsApi.md#get_product_assets) | **GET** /retailer/products/{ean}/assets | Get product assets
[**get_product_ids**](ProductsApi.md#get_product_ids) | **GET** /retailer/products/{ean}/product-ids | Get product ids by EAN
[**get_product_list**](ProductsApi.md#get_product_list) | **POST** /retailer/products/list | Get product list
[**get_product_list_filters**](ProductsApi.md#get_product_list_filters) | **GET** /retailer/products/list-filters | Get product list filters
[**get_product_placement**](ProductsApi.md#get_product_placement) | **GET** /retailer/products/{ean}/placement | Get product placement
[**get_product_ratings**](ProductsApi.md#get_product_ratings) | **GET** /retailer/products/{ean}/ratings | Get product ratings


# **get_competing_offers**
> CompetingOffersResponse get_competing_offers(ean, page=page, country_code=country_code, best_offer_only=best_offer_only, condition=condition)

Get a list of competing offers by EAN

Use this endpoint to get a list of offers available in the webshop. The list includes offers for all retailers.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.competing_offers_response import CompetingOffersResponse
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
    api_instance = openapi_client.ProductsApi(api_client)
    ean = '0000007740404' # str | The EAN number associated with this product.
    page = 1 # int | The requested page number with a page size of 50 items. (optional) (default to 1)
    country_code = 'NL' # str | Countries in which this offer is currently on sale in the webshop, in ISO-3166-1 format. (optional)
    best_offer_only = False # bool | Indicator to request the best offer within the country for the requested EAN. (optional) (default to False)
    condition = 'NEW' # str | The condition of the offered product. (optional)

    try:
        # Get a list of competing offers by EAN
        api_response = api_instance.get_competing_offers(ean, page=page, country_code=country_code, best_offer_only=best_offer_only, condition=condition)
        print("The response of ProductsApi->get_competing_offers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->get_competing_offers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ean** | **str**| The EAN number associated with this product. | 
 **page** | **int**| The requested page number with a page size of 50 items. | [optional] [default to 1]
 **country_code** | **str**| Countries in which this offer is currently on sale in the webshop, in ISO-3166-1 format. | [optional] 
 **best_offer_only** | **bool**| Indicator to request the best offer within the country for the requested EAN. | [optional] [default to False]
 **condition** | **str**| The condition of the offered product. | [optional] 

### Return type

[**CompetingOffersResponse**](CompetingOffersResponse.md)

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

# **get_price_star_boundaries**
> PriceStarBoundaries get_price_star_boundaries(ean)

Get price star boundaries by EAN

Gets a list of all price star boundaries for a specific EAN.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.price_star_boundaries import PriceStarBoundaries
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
    api_instance = openapi_client.ProductsApi(api_client)
    ean = '0000007740404' # str | The EAN number associated with this product.

    try:
        # Get price star boundaries by EAN
        api_response = api_instance.get_price_star_boundaries(ean)
        print("The response of ProductsApi->get_price_star_boundaries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->get_price_star_boundaries: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ean** | **str**| The EAN number associated with this product. | 

### Return type

[**PriceStarBoundaries**](PriceStarBoundaries.md)

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

# **get_product_assets**
> ProductAssetsResponse get_product_assets(ean, usage=usage)

Get product assets

Gets the list of asset available for the product by EAN.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.product_assets_response import ProductAssetsResponse
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
    api_instance = openapi_client.ProductsApi(api_client)
    ean = '0000007740404' # str | The EAN number associated with this product.
    usage = 'ADDITIONAL' # str | Type of the asset being used for. (optional)

    try:
        # Get product assets
        api_response = api_instance.get_product_assets(ean, usage=usage)
        print("The response of ProductsApi->get_product_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->get_product_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ean** | **str**| The EAN number associated with this product. | 
 **usage** | **str**| Type of the asset being used for. | [optional] 

### Return type

[**ProductAssetsResponse**](ProductAssetsResponse.md)

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

# **get_product_ids**
> ProductIdsResponse get_product_ids(ean)

Get product ids by EAN

Get the bol.com specific product identifier and the related EANs.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.product_ids_response import ProductIdsResponse
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
    api_instance = openapi_client.ProductsApi(api_client)
    ean = '0000007740404' # str | The EAN number associated with this product.

    try:
        # Get product ids by EAN
        api_response = api_instance.get_product_ids(ean)
        print("The response of ProductsApi->get_product_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->get_product_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ean** | **str**| The EAN number associated with this product. | 

### Return type

[**ProductIdsResponse**](ProductIdsResponse.md)

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

# **get_product_list**
> ProductListResponse get_product_list(product_list_request, accept_language=accept_language)

Get product list

Gets the list of products based on category, search term or filters.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.product_list_request import ProductListRequest
from openapi_client.models.product_list_response import ProductListResponse
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
    api_instance = openapi_client.ProductsApi(api_client)
    product_list_request = openapi_client.ProductListRequest() # ProductListRequest | 
    accept_language = 'nl' # str | The language in which the product list will be retrieved. (optional)

    try:
        # Get product list
        api_response = api_instance.get_product_list(product_list_request, accept_language=accept_language)
        print("The response of ProductsApi->get_product_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->get_product_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_list_request** | [**ProductListRequest**](ProductListRequest.md)|  | 
 **accept_language** | **str**| The language in which the product list will be retrieved. | [optional] 

### Return type

[**ProductListResponse**](ProductListResponse.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/vnd.retailer.v10+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok: Successfully processed the request. |  -  |
**400** | Bad request: The sent request does not meet the API specification. Please check the error message(s) for more information. |  -  |
**404** | Not found: The requested item could not be found. |  -  |
**406** | Not acceptable: The sent request header does not meet the API specification. Please check the error message(s) for more information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_list_filters**
> ProductListFiltersResponse get_product_list_filters(product_list_filters_request, country_code=country_code, search_term=search_term, category_id=category_id, accept_language=accept_language)

Get product list filters

Gets the list of possible filters for products based on category or search term.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.product_list_filters_request import ProductListFiltersRequest
from openapi_client.models.product_list_filters_response import ProductListFiltersResponse
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
    api_instance = openapi_client.ProductsApi(api_client)
    product_list_filters_request = openapi_client.ProductListFiltersRequest() # ProductListFiltersRequest | 
    country_code = 'NL' # str | The country for which the filters will be retrieved. (optional)
    search_term = 'pen' # str | The search-term to get the associated categories and filters for. (optional)
    category_id = '10505' # str | The category to get the associated filters for. (optional)
    accept_language = 'nl' # str | The language in which the product list filters will be retrieved. (optional)

    try:
        # Get product list filters
        api_response = api_instance.get_product_list_filters(product_list_filters_request, country_code=country_code, search_term=search_term, category_id=category_id, accept_language=accept_language)
        print("The response of ProductsApi->get_product_list_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->get_product_list_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_list_filters_request** | [**ProductListFiltersRequest**](.md)|  | 
 **country_code** | **str**| The country for which the filters will be retrieved. | [optional] 
 **search_term** | **str**| The search-term to get the associated categories and filters for. | [optional] 
 **category_id** | **str**| The category to get the associated filters for. | [optional] 
 **accept_language** | **str**| The language in which the product list filters will be retrieved. | [optional] 

### Return type

[**ProductListFiltersResponse**](ProductListFiltersResponse.md)

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
**406** | Not acceptable: The sent request header does not meet the API specification. Please check the error message(s) for more information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_placement**
> ProductPlacementResponse get_product_placement(ean, country_code=country_code, accept_language=accept_language)

Get product placement

Gets the list of categories and the URL where the product is placed in the webshop.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.product_placement_response import ProductPlacementResponse
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
    api_instance = openapi_client.ProductsApi(api_client)
    ean = '0000007740404' # str | The EAN number associated with this product.
    country_code = 'NL' # str | The country of the product placed on the webshop. (optional)
    accept_language = 'nl' # str | The language in which the product categories and URL will be retrieved. (optional)

    try:
        # Get product placement
        api_response = api_instance.get_product_placement(ean, country_code=country_code, accept_language=accept_language)
        print("The response of ProductsApi->get_product_placement:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->get_product_placement: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ean** | **str**| The EAN number associated with this product. | 
 **country_code** | **str**| The country of the product placed on the webshop. | [optional] 
 **accept_language** | **str**| The language in which the product categories and URL will be retrieved. | [optional] 

### Return type

[**ProductPlacementResponse**](ProductPlacementResponse.md)

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
**406** | Not acceptable: The sent request header does not meet the API specification. Please check the error message(s) for more information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_ratings**
> ProductRatingsResponse get_product_ratings(ean)

Get product ratings

Gets a list of ratings for the products associated with the provided EAN.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.product_ratings_response import ProductRatingsResponse
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
    api_instance = openapi_client.ProductsApi(api_client)
    ean = '0000007740404' # str | The EAN number associated with this rating.

    try:
        # Get product ratings
        api_response = api_instance.get_product_ratings(ean)
        print("The response of ProductsApi->get_product_ratings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductsApi->get_product_ratings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ean** | **str**| The EAN number associated with this rating. | 

### Return type

[**ProductRatingsResponse**](ProductRatingsResponse.md)

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

