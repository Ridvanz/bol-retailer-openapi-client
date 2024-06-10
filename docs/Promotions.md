# Promotions

Container for multiple promotions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**promotions** | [**List[ReducedPromotion]**](ReducedPromotion.md) |  | [optional] 

## Example

```python
from openapi_client.models.promotions import Promotions

# TODO update the JSON string below
json = "{}"
# create an instance of Promotions from a JSON string
promotions_instance = Promotions.from_json(json)
# print the JSON string representation of the object
print(Promotions.to_json())

# convert the object into a dict
promotions_dict = promotions_instance.to_dict()
# create an instance of Promotions from a dict
promotions_from_dict = Promotions.from_dict(promotions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


