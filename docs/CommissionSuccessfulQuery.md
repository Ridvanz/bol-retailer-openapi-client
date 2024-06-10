# CommissionSuccessfulQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **float** | This provides the location of the entity where it was provided in the original response body. | 
**status** | **int** | HTTP status code for individual entity operation. | 
**commission_rates** | [**List[CommissionRate]**](CommissionRate.md) |  | 

## Example

```python
from openapi_client.models.commission_successful_query import CommissionSuccessfulQuery

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionSuccessfulQuery from a JSON string
commission_successful_query_instance = CommissionSuccessfulQuery.from_json(json)
# print the JSON string representation of the object
print(CommissionSuccessfulQuery.to_json())

# convert the object into a dict
commission_successful_query_dict = commission_successful_query_instance.to_dict()
# create an instance of CommissionSuccessfulQuery from a dict
commission_successful_query_from_dict = CommissionSuccessfulQuery.from_dict(commission_successful_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


