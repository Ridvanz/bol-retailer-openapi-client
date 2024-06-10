# ReducedReturn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_id** | **str** | Unique identifier for a return. | 
**registration_date_time** | **datetime** | The date and time in ISO 8601 format when this return was registered. | 
**fulfilment_method** | **str** | The fulfilment method. Fulfilled by the retailer (FBR) or fulfilled by bol.com (FBB). | 
**return_items** | [**List[ReducedReturnItem]**](ReducedReturnItem.md) |  | 

## Example

```python
from openapi_client.models.reduced_return import ReducedReturn

# TODO update the JSON string below
json = "{}"
# create an instance of ReducedReturn from a JSON string
reduced_return_instance = ReducedReturn.from_json(json)
# print the JSON string representation of the object
print(ReducedReturn.to_json())

# convert the object into a dict
reduced_return_dict = reduced_return_instance.to_dict()
# create an instance of ReducedReturn from a dict
reduced_return_from_dict = ReducedReturn.from_dict(reduced_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


