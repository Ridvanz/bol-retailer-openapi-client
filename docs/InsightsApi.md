# openapi_client.InsightsApi

All URIs are relative to *https://api.bol.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_offer_insights**](InsightsApi.md#get_offer_insights) | **GET** /retailer/insights/offer | Get offer insights
[**get_performance_indicators**](InsightsApi.md#get_performance_indicators) | **GET** /retailer/insights/performance/indicator | Get performance indicators
[**get_product_ranks**](InsightsApi.md#get_product_ranks) | **GET** /retailer/insights/product-ranks | Get product ranks
[**get_sales_forecast**](InsightsApi.md#get_sales_forecast) | **GET** /retailer/insights/sales-forecast | Get sales forecast
[**get_search_terms**](InsightsApi.md#get_search_terms) | **GET** /retailer/insights/search-terms | Get search terms


# **get_offer_insights**
> OfferInsights get_offer_insights(offer_id, period, number_of_periods, name)

Get offer insights

Get the product visits and the buy box percentage for an offer during a given period.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.offer_insights import OfferInsights
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
    api_instance = openapi_client.InsightsApi(api_client)
    offer_id = 'offer_id_example' # str | Unique identifier for an offer.
    period = 'period_example' # str | The time unit in which the offer insights are grouped.
    number_of_periods = 56 # int | The number of periods for which the offer insights are requested back in time. The maximum available periods are 24 for MONTH, 104 for WEEK, and 730 for DAY.
    name = 'name_example' # str | The name of the requested offer insight.

    try:
        # Get offer insights
        api_response = api_instance.get_offer_insights(offer_id, period, number_of_periods, name)
        print("The response of InsightsApi->get_offer_insights:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InsightsApi->get_offer_insights: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| Unique identifier for an offer. | 
 **period** | **str**| The time unit in which the offer insights are grouped. | 
 **number_of_periods** | **int**| The number of periods for which the offer insights are requested back in time. The maximum available periods are 24 for MONTH, 104 for WEEK, and 730 for DAY. | 
 **name** | **str**| The name of the requested offer insight. | 

### Return type

[**OfferInsights**](OfferInsights.md)

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

# **get_performance_indicators**
> PerformanceIndicators get_performance_indicators(name, year, week)

Get performance indicators

Gets the measurements for your performance indicators per week.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.performance_indicators import PerformanceIndicators
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
    api_instance = openapi_client.InsightsApi(api_client)
    name = 'name_example' # str | The type of the performance indicator
    year = 'year_example' # str | Year number in the ISO-8601 standard.
    week = 'week_example' # str | Week number in the ISO-8601 standard. If you would like to get the relative scores from the current week, please provide the current week number here. Be advised that measurements can change heavily over the course of the week.

    try:
        # Get performance indicators
        api_response = api_instance.get_performance_indicators(name, year, week)
        print("The response of InsightsApi->get_performance_indicators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InsightsApi->get_performance_indicators: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The type of the performance indicator | 
 **year** | **str**| Year number in the ISO-8601 standard. | 
 **week** | **str**| Week number in the ISO-8601 standard. If you would like to get the relative scores from the current week, please provide the current week number here. Be advised that measurements can change heavily over the course of the week. | 

### Return type

[**PerformanceIndicators**](PerformanceIndicators.md)

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

# **get_product_ranks**
> ProductRanks get_product_ranks(ean, var_date, type=type, page=page, accept_language=accept_language)

Get product ranks

Gets a list of product ranks.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.product_ranks import ProductRanks
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
    api_instance = openapi_client.InsightsApi(api_client)
    ean = 'ean_example' # str | The EAN number associated with this product.
    var_date = 'var_date_example' # str | Filters search results to a specific date. The date must be in the past, no more than three months back, and up to yesterday.
    type = 'type_example' # str | Determines the search type, either 'SEARCH' for specific queries or 'BROWSE' for broader category searches. In order to retrieve all results, it can be sent as \"null\". (optional)
    page = 1 # int | The requested page number with a page size of 50 items. (optional) (default to 1)
    accept_language = 'accept_language_example' # str | The language to search for. (optional)

    try:
        # Get product ranks
        api_response = api_instance.get_product_ranks(ean, var_date, type=type, page=page, accept_language=accept_language)
        print("The response of InsightsApi->get_product_ranks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InsightsApi->get_product_ranks: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ean** | **str**| The EAN number associated with this product. | 
 **var_date** | **str**| Filters search results to a specific date. The date must be in the past, no more than three months back, and up to yesterday. | 
 **type** | **str**| Determines the search type, either &#39;SEARCH&#39; for specific queries or &#39;BROWSE&#39; for broader category searches. In order to retrieve all results, it can be sent as \&quot;null\&quot;. | [optional] 
 **page** | **int**| The requested page number with a page size of 50 items. | [optional] [default to 1]
 **accept_language** | **str**| The language to search for. | [optional] 

### Return type

[**ProductRanks**](ProductRanks.md)

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
**406** | Not acceptable: The sent request header does not meet the API specification. Please check the error message(s) for more information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_forecast**
> SalesForecastResponse get_sales_forecast(offer_id, weeks_ahead)

Get sales forecast

Get sales forecast to estimate the sales expectations on the total bol.com platform for the requested number of weeks ahead.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.sales_forecast_response import SalesForecastResponse
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
    api_instance = openapi_client.InsightsApi(api_client)
    offer_id = 'offer_id_example' # str | Unique identifier for an offer.
    weeks_ahead = 56 # int | The number of weeks into the future, starting from today.

    try:
        # Get sales forecast
        api_response = api_instance.get_sales_forecast(offer_id, weeks_ahead)
        print("The response of InsightsApi->get_sales_forecast:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InsightsApi->get_sales_forecast: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| Unique identifier for an offer. | 
 **weeks_ahead** | **int**| The number of weeks into the future, starting from today. | 

### Return type

[**SalesForecastResponse**](SalesForecastResponse.md)

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

# **get_search_terms**
> SearchTerms get_search_terms(search_term, period, number_of_periods, related_search_terms=related_search_terms)

Get search terms

Retrieves the search volume for a specified search term and period. The search volume allows you to see what bol.com customers are searching for. Based on the search volume per search term you can optimize your product content, or spot opportunities to extend your assortment, or analyzing trends for inventory management.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.search_terms import SearchTerms
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
    api_instance = openapi_client.InsightsApi(api_client)
    search_term = 'search_term_example' # str | The search term for which you want to request the search volume.
    period = 'period_example' # str | The time unit in which the offer insights are grouped.
    number_of_periods = 56 # int | The number of periods for which the offer insights are requested back in time.
    related_search_terms = False # bool | Indicates whether or not you want to retrieve the related search terms. (optional) (default to False)

    try:
        # Get search terms
        api_response = api_instance.get_search_terms(search_term, period, number_of_periods, related_search_terms=related_search_terms)
        print("The response of InsightsApi->get_search_terms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InsightsApi->get_search_terms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **search_term** | **str**| The search term for which you want to request the search volume. | 
 **period** | **str**| The time unit in which the offer insights are grouped. | 
 **number_of_periods** | **int**| The number of periods for which the offer insights are requested back in time. | 
 **related_search_terms** | **bool**| Indicates whether or not you want to retrieve the related search terms. | [optional] [default to False]

### Return type

[**SearchTerms**](SearchTerms.md)

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

