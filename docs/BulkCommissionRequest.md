# BulkCommissionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**commission_queries** | [**List[BulkCommissionQuery]**](BulkCommissionQuery.md) |  | 

## Example

```python
from openapi_client.models.bulk_commission_request import BulkCommissionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCommissionRequest from a JSON string
bulk_commission_request_instance = BulkCommissionRequest.from_json(json)
# print the JSON string representation of the object
print(BulkCommissionRequest.to_json())

# convert the object into a dict
bulk_commission_request_dict = bulk_commission_request_instance.to_dict()
# create an instance of BulkCommissionRequest from a dict
bulk_commission_request_from_dict = BulkCommissionRequest.from_dict(bulk_commission_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


