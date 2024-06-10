# Norm

Service norm for this indicator.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition** | **str** | Condition norm for this indicator. | 
**value** | **float** | Service norm for this indicator. | 

## Example

```python
from openapi_client.models.norm import Norm

# TODO update the JSON string below
json = "{}"
# create an instance of Norm from a JSON string
norm_instance = Norm.from_json(json)
# print the JSON string representation of the object
print(Norm.to_json())

# convert the object into a dict
norm_dict = norm_instance.to_dict()
# create an instance of Norm from a dict
norm_from_dict = Norm.from_dict(norm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


