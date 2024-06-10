# openapi_client.OffersApi

All URIs are relative to *https://api.bol.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_offer**](OffersApi.md#delete_offer) | **DELETE** /retailer/offers/{offer-id} | Delete offer by id
[**get_offer**](OffersApi.md#get_offer) | **GET** /retailer/offers/{offer-id} | Retrieve an offer by its offer id
[**get_offer_export**](OffersApi.md#get_offer_export) | **GET** /retailer/offers/export/{report-id} | Retrieve an offer export file by report id
[**get_unpublished_offer_report**](OffersApi.md#get_unpublished_offer_report) | **GET** /retailer/offers/unpublished/{report-id} | Retrieve an unpublished offer report by report id
[**post_offer**](OffersApi.md#post_offer) | **POST** /retailer/offers | Create a new offer
[**post_offer_export**](OffersApi.md#post_offer_export) | **POST** /retailer/offers/export | Request an offer export file
[**post_unpublished_offer_report**](OffersApi.md#post_unpublished_offer_report) | **POST** /retailer/offers/unpublished | Request an unpublished offer report
[**put_offer**](OffersApi.md#put_offer) | **PUT** /retailer/offers/{offer-id} | Update an offer
[**update_offer_price**](OffersApi.md#update_offer_price) | **PUT** /retailer/offers/{offer-id}/price | Update price(s) for offer by id
[**update_offer_stock**](OffersApi.md#update_offer_stock) | **PUT** /retailer/offers/{offer-id}/stock | Update stock for offer by id


# **delete_offer**
> ProcessStatus delete_offer(offer_id)

Delete offer by id

Delete an offer by id.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
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
    api_instance = openapi_client.OffersApi(api_client)
    offer_id = 'offer_id_example' # str | Unique identifier for an offer.

    try:
        # Delete offer by id
        api_response = api_instance.delete_offer(offer_id)
        print("The response of OffersApi->delete_offer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffersApi->delete_offer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| Unique identifier for an offer. | 

### Return type

[**ProcessStatus**](ProcessStatus.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.retailer.v10+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted: Successfully scheduled the request for processing. |  -  |
**400** | Bad request: The sent request does not meet the API specification. Please check the error message(s) for more information. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_offer**
> RetailerOffer get_offer(offer_id)

Retrieve an offer by its offer id

Retrieve an offer by using the offer id provided to you when creating or listing your offers.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.retailer_offer import RetailerOffer
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
    api_instance = openapi_client.OffersApi(api_client)
    offer_id = 'offer_id_example' # str | Unique identifier for an offer.

    try:
        # Retrieve an offer by its offer id
        api_response = api_instance.get_offer(offer_id)
        print("The response of OffersApi->get_offer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffersApi->get_offer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| Unique identifier for an offer. | 

### Return type

[**RetailerOffer**](RetailerOffer.md)

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

# **get_offer_export**
> get_offer_export(report_id)

Retrieve an offer export file by report id

Retrieve an offer export file containing all offers.

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
    api_instance = openapi_client.OffersApi(api_client)
    report_id = 'report_id_example' # str | Unique identifier for an offer export file.

    try:
        # Retrieve an offer export file by report id
        api_instance.get_offer_export(report_id)
    except Exception as e:
        print("Exception when calling OffersApi->get_offer_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| Unique identifier for an offer export file. | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.retailer.v10+csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok: Successfully processed the request. |  -  |
**400** | Bad request: The sent request does not meet the API specification. Please check the error message(s) for more information. |  -  |
**404** | Not found: The requested item could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unpublished_offer_report**
> get_unpublished_offer_report(report_id)

Retrieve an unpublished offer report by report id

Retrieve an unpublished offer report containing all unpublished offers and reasons.

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
    api_instance = openapi_client.OffersApi(api_client)
    report_id = 'report_id_example' # str | Unique identifier for unpublished offer report.

    try:
        # Retrieve an unpublished offer report by report id
        api_instance.get_unpublished_offer_report(report_id)
    except Exception as e:
        print("Exception when calling OffersApi->get_unpublished_offer_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **report_id** | **str**| Unique identifier for unpublished offer report. | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/vnd.retailer.v10+csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok: Successfully processed the request. |  -  |
**400** | Bad request: The sent request does not meet the API specification. Please check the error message(s) for more information. |  -  |
**404** | Not found: The requested item could not be found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_offer**
> ProcessStatus post_offer(create_offer_request)

Create a new offer

Creates a new offer, and adds it to the catalog. After creation, status information can be retrieved to review if the offer is valid and published to the shop.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.create_offer_request import CreateOfferRequest
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
    api_instance = openapi_client.OffersApi(api_client)
    create_offer_request = openapi_client.CreateOfferRequest() # CreateOfferRequest | 

    try:
        # Create a new offer
        api_response = api_instance.post_offer(create_offer_request)
        print("The response of OffersApi->post_offer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffersApi->post_offer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_offer_request** | [**CreateOfferRequest**](CreateOfferRequest.md)|  | 

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

# **post_offer_export**
> ProcessStatus post_offer_export(create_offer_export_request)

Request an offer export file

Request an offer export file containing all offers.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.create_offer_export_request import CreateOfferExportRequest
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
    api_instance = openapi_client.OffersApi(api_client)
    create_offer_export_request = openapi_client.CreateOfferExportRequest() # CreateOfferExportRequest | 

    try:
        # Request an offer export file
        api_response = api_instance.post_offer_export(create_offer_export_request)
        print("The response of OffersApi->post_offer_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffersApi->post_offer_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_offer_export_request** | [**CreateOfferExportRequest**](CreateOfferExportRequest.md)|  | 

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

# **post_unpublished_offer_report**
> ProcessStatus post_unpublished_offer_report(create_unpublished_offer_report_request)

Request an unpublished offer report

Request an unpublished offer report containing all unpublished offers and reasons.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.create_unpublished_offer_report_request import CreateUnpublishedOfferReportRequest
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
    api_instance = openapi_client.OffersApi(api_client)
    create_unpublished_offer_report_request = openapi_client.CreateUnpublishedOfferReportRequest() # CreateUnpublishedOfferReportRequest | 

    try:
        # Request an unpublished offer report
        api_response = api_instance.post_unpublished_offer_report(create_unpublished_offer_report_request)
        print("The response of OffersApi->post_unpublished_offer_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffersApi->post_unpublished_offer_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_unpublished_offer_report_request** | [**CreateUnpublishedOfferReportRequest**](CreateUnpublishedOfferReportRequest.md)|  | 

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

# **put_offer**
> ProcessStatus put_offer(offer_id, update_offer_request)

Update an offer

Use this endpoint to send an offer update. This endpoint returns a process status.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.process_status import ProcessStatus
from openapi_client.models.update_offer_request import UpdateOfferRequest
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
    api_instance = openapi_client.OffersApi(api_client)
    offer_id = 'offer_id_example' # str | Unique identifier for an offer.
    update_offer_request = openapi_client.UpdateOfferRequest() # UpdateOfferRequest | 

    try:
        # Update an offer
        api_response = api_instance.put_offer(offer_id, update_offer_request)
        print("The response of OffersApi->put_offer:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffersApi->put_offer: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| Unique identifier for an offer. | 
 **update_offer_request** | [**UpdateOfferRequest**](UpdateOfferRequest.md)|  | 

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

# **update_offer_price**
> ProcessStatus update_offer_price(offer_id, update_offer_price_request)

Update price(s) for offer by id

Update price(s) for offer by id.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.process_status import ProcessStatus
from openapi_client.models.update_offer_price_request import UpdateOfferPriceRequest
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
    api_instance = openapi_client.OffersApi(api_client)
    offer_id = 'offer_id_example' # str | Unique identifier for an offer.
    update_offer_price_request = openapi_client.UpdateOfferPriceRequest() # UpdateOfferPriceRequest | 

    try:
        # Update price(s) for offer by id
        api_response = api_instance.update_offer_price(offer_id, update_offer_price_request)
        print("The response of OffersApi->update_offer_price:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffersApi->update_offer_price: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| Unique identifier for an offer. | 
 **update_offer_price_request** | [**UpdateOfferPriceRequest**](UpdateOfferPriceRequest.md)|  | 

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

# **update_offer_stock**
> ProcessStatus update_offer_stock(offer_id, update_offer_stock_request)

Update stock for offer by id

Update stock for offer by id.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.process_status import ProcessStatus
from openapi_client.models.update_offer_stock_request import UpdateOfferStockRequest
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
    api_instance = openapi_client.OffersApi(api_client)
    offer_id = 'offer_id_example' # str | Unique identifier for an offer.
    update_offer_stock_request = openapi_client.UpdateOfferStockRequest() # UpdateOfferStockRequest | 

    try:
        # Update stock for offer by id
        api_response = api_instance.update_offer_stock(offer_id, update_offer_stock_request)
        print("The response of OffersApi->update_offer_stock:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OffersApi->update_offer_stock: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_id** | **str**| Unique identifier for an offer. | 
 **update_offer_stock_request** | [**UpdateOfferStockRequest**](UpdateOfferStockRequest.md)|  | 

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

