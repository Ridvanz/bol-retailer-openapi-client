# BulkCommissionRatesMultiStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**successful_queries** | [**List[CommissionSuccessfulQuery]**](CommissionSuccessfulQuery.md) |  | 
**failed_queries** | [**List[CommissionFailedQuery]**](CommissionFailedQuery.md) |  | 

## Example

```python
from openapi_client.models.bulk_commission_rates_multi_status_response import BulkCommissionRatesMultiStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCommissionRatesMultiStatusResponse from a JSON string
bulk_commission_rates_multi_status_response_instance = BulkCommissionRatesMultiStatusResponse.from_json(json)
# print the JSON string representation of the object
print(BulkCommissionRatesMultiStatusResponse.to_json())

# convert the object into a dict
bulk_commission_rates_multi_status_response_dict = bulk_commission_rates_multi_status_response_instance.to_dict()
# create an instance of BulkCommissionRatesMultiStatusResponse from a dict
bulk_commission_rates_multi_status_response_from_dict = BulkCommissionRatesMultiStatusResponse.from_dict(bulk_commission_rates_multi_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


