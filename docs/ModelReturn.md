# ModelReturn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_id** | **str** | Unique identifier for a return. | 
**registration_date_time** | **datetime** | The date and time in ISO 8601 format when this return was registered. | 
**fulfilment_method** | **str** | The fulfilment method. Fulfilled by the retailer (FBR) or fulfilled by bol.com (FBB). | 
**return_items** | [**List[ReturnItem]**](ReturnItem.md) |  | 

## Example

```python
from openapi_client.models.model_return import ModelReturn

# TODO update the JSON string below
json = "{}"
# create an instance of ModelReturn from a JSON string
model_return_instance = ModelReturn.from_json(json)
# print the JSON string representation of the object
print(ModelReturn.to_json())

# convert the object into a dict
model_return_dict = model_return_instance.to_dict()
# create an instance of ModelReturn from a dict
model_return_from_dict = ModelReturn.from_dict(model_return_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


