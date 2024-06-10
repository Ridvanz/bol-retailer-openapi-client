# Promotion

A single promotion.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**promotion_id** | **str** | The identifier of the promotion. | 
**title** | **str** | The title of the promotion. | 
**start_date_time** | **datetime** | The starting date and time of the promotion. | 
**end_date_time** | **datetime** | The ending date and time of the promotion. | 
**countries** | [**List[PromotionCountryCode]**](PromotionCountryCode.md) |  | 
**promotion_type** | **str** | The type of the promotion. | 
**retailer_specific_promotion** | **bool** | Indicates whether the promotion is retailer specific or open to the platform. | 
**campaign** | [**Campaign**](Campaign.md) |  | [optional] 

## Example

```python
from openapi_client.models.promotion import Promotion

# TODO update the JSON string below
json = "{}"
# create an instance of Promotion from a JSON string
promotion_instance = Promotion.from_json(json)
# print the JSON string representation of the object
print(Promotion.to_json())

# convert the object into a dict
promotion_dict = promotion_instance.to_dict()
# create an instance of Promotion from a dict
promotion_from_dict = Promotion.from_dict(promotion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


