# CommissionFailedQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **float** | This provides the location of the entity where it was provided in the original response body. | 
**status** | **int** | HTTP status code for individual entity operation. | 
**violations** | [**List[Violation]**](Violation.md) | Outlines the list of violations encountered in the API for the specific index detailing the nature and reason for the issue. | 

## Example

```python
from openapi_client.models.commission_failed_query import CommissionFailedQuery

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionFailedQuery from a JSON string
commission_failed_query_instance = CommissionFailedQuery.from_json(json)
# print the JSON string representation of the object
print(CommissionFailedQuery.to_json())

# convert the object into a dict
commission_failed_query_dict = commission_failed_query_instance.to_dict()
# create an instance of CommissionFailedQuery from a dict
commission_failed_query_from_dict = CommissionFailedQuery.from_dict(commission_failed_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


