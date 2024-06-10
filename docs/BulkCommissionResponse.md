# BulkCommissionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commissions** | [**List[Commission]**](Commission.md) |  | 

## Example

```python
from openapi_client.models.bulk_commission_response import BulkCommissionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCommissionResponse from a JSON string
bulk_commission_response_instance = BulkCommissionResponse.from_json(json)
# print the JSON string representation of the object
print(BulkCommissionResponse.to_json())

# convert the object into a dict
bulk_commission_response_dict = bulk_commission_response_instance.to_dict()
# create an instance of BulkCommissionResponse from a dict
bulk_commission_response_from_dict = BulkCommissionResponse.from_dict(bulk_commission_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


