# openapi_client.ProductContentApi

All URIs are relative to *https://api.bol.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_catalog_product**](ProductContentApi.md#get_catalog_product) | **GET** /retailer/content/catalog-products/{ean} | Get catalog product details by EAN
[**get_chunk_recommendations**](ProductContentApi.md#get_chunk_recommendations) | **POST** /retailer/content/chunk-recommendations | Get chunk recommendations
[**get_upload_report**](ProductContentApi.md#get_upload_report) | **GET** /retailer/content/upload-report/{upload-id} | Get an upload report by upload id
[**post_product_content**](ProductContentApi.md#post_product_content) | **POST** /retailer/content/products | Create content for a product


# **get_catalog_product**
> CatalogProduct get_catalog_product(ean, accept_language=accept_language)

Get catalog product details by EAN

Gets the details of a catalog product by means of its EAN.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.catalog_product import CatalogProduct
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
    api_instance = openapi_client.ProductContentApi(api_client)
    ean = '0000007740404' # str | The EAN number associated with this product.
    accept_language = 'nl' # str | The language in which the catalog product details will be retrieved. (optional)

    try:
        # Get catalog product details by EAN
        api_response = api_instance.get_catalog_product(ean, accept_language=accept_language)
        print("The response of ProductContentApi->get_catalog_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductContentApi->get_catalog_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ean** | **str**| The EAN number associated with this product. | 
 **accept_language** | **str**| The language in which the catalog product details will be retrieved. | [optional] 

### Return type

[**CatalogProduct**](CatalogProduct.md)

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

# **get_chunk_recommendations**
> ChunkRecommendationsResponse get_chunk_recommendations(chunk_recommendations_request)

Get chunk recommendations

Gets a selected number of recommendations for a product.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.chunk_recommendations_request import ChunkRecommendationsRequest
from openapi_client.models.chunk_recommendations_response import ChunkRecommendationsResponse
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
    api_instance = openapi_client.ProductContentApi(api_client)
    chunk_recommendations_request = openapi_client.ChunkRecommendationsRequest() # ChunkRecommendationsRequest | 

    try:
        # Get chunk recommendations
        api_response = api_instance.get_chunk_recommendations(chunk_recommendations_request)
        print("The response of ProductContentApi->get_chunk_recommendations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductContentApi->get_chunk_recommendations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chunk_recommendations_request** | [**ChunkRecommendationsRequest**](ChunkRecommendationsRequest.md)|  | 

### Return type

[**ChunkRecommendationsResponse**](ChunkRecommendationsResponse.md)

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

# **get_upload_report**
> UploadReportResponse get_upload_report(upload_id)

Get an upload report by upload id

Gets the upload report of the product content submitted by upload id.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.upload_report_response import UploadReportResponse
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
    api_instance = openapi_client.ProductContentApi(api_client)
    upload_id = 'upload_id_example' # str | The identifier of the upload report.

    try:
        # Get an upload report by upload id
        api_response = api_instance.get_upload_report(upload_id)
        print("The response of ProductContentApi->get_upload_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductContentApi->get_upload_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload_id** | **str**| The identifier of the upload report. | 

### Return type

[**UploadReportResponse**](UploadReportResponse.md)

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

# **post_product_content**
> ProcessStatus post_product_content(create_product_content_single_request)

Create content for a product

Create content for an existing product.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.create_product_content_single_request import CreateProductContentSingleRequest
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
    api_instance = openapi_client.ProductContentApi(api_client)
    create_product_content_single_request = openapi_client.CreateProductContentSingleRequest() # CreateProductContentSingleRequest | 

    try:
        # Create content for a product
        api_response = api_instance.post_product_content(create_product_content_single_request)
        print("The response of ProductContentApi->post_product_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProductContentApi->post_product_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_product_content_single_request** | [**CreateProductContentSingleRequest**](CreateProductContentSingleRequest.md)|  | 

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

