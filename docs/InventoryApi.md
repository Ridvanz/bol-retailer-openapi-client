# openapi_client.InventoryApi

All URIs are relative to *https://api.bol.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_inventory**](InventoryApi.md#get_inventory) | **GET** /retailer/inventory | Get LVB/FBB inventory


# **get_inventory**
> InventoryResponse get_inventory(page=page, quantity=quantity, stock=stock, state=state, query=query)

Get LVB/FBB inventory

The inventory endpoint is a specific LVB/FBB endpoint. It provides a paginated list containing your fulfilment by bol.com inventory. This endpoint does not provide information about your own stock.

### Example

* Bearer Authentication (OAuth2):

```python
import openapi_client
from openapi_client.models.inventory_response import InventoryResponse
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
    api_instance = openapi_client.InventoryApi(api_client)
    page = 1 # int | The requested page number with a page size of 50 items. (optional) (default to 1)
    quantity = ['0-10,20-30'] # List[str] | Filter inventory by providing a range of quantity (min-range)-(max-range). Note that if no state query is submitted in the same request, then the quantity will be filtered on regularStock by default. (optional)
    stock = 'SUFFICIENT' # str | Filter inventory by stock level. (optional)
    state = 'REGULAR' # str | Filter inventory by stock type. (optional)
    query = '0000007740404' # str | Filter inventory by EAN or product title. (optional)

    try:
        # Get LVB/FBB inventory
        api_response = api_instance.get_inventory(page=page, quantity=quantity, stock=stock, state=state, query=query)
        print("The response of InventoryApi->get_inventory:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryApi->get_inventory: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The requested page number with a page size of 50 items. | [optional] [default to 1]
 **quantity** | [**List[str]**](str.md)| Filter inventory by providing a range of quantity (min-range)-(max-range). Note that if no state query is submitted in the same request, then the quantity will be filtered on regularStock by default. | [optional] 
 **stock** | **str**| Filter inventory by stock level. | [optional] 
 **state** | **str**| Filter inventory by stock type. | [optional] 
 **query** | **str**| Filter inventory by EAN or product title. | [optional] 

### Return type

[**InventoryResponse**](InventoryResponse.md)

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

