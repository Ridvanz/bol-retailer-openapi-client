# ReplenishmentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**replenishments** | [**List[ReducedReplenishment]**](ReducedReplenishment.md) |  | 

## Example

```python
from openapi_client.models.replenishments_response import ReplenishmentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ReplenishmentsResponse from a JSON string
replenishments_response_instance = ReplenishmentsResponse.from_json(json)
# print the JSON string representation of the object
print(ReplenishmentsResponse.to_json())

# convert the object into a dict
replenishments_response_dict = replenishments_response_instance.to_dict()
# create an instance of ReplenishmentsResponse from a dict
replenishments_response_from_dict = ReplenishmentsResponse.from_dict(replenishments_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


