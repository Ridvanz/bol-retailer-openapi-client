# PromotionCountryCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | The country code of the country in which the promotion is active. | 

## Example

```python
from openapi_client.models.promotion_country_code import PromotionCountryCode

# TODO update the JSON string below
json = "{}"
# create an instance of PromotionCountryCode from a JSON string
promotion_country_code_instance = PromotionCountryCode.from_json(json)
# print the JSON string representation of the object
print(PromotionCountryCode.to_json())

# convert the object into a dict
promotion_country_code_dict = promotion_country_code_instance.to_dict()
# create an instance of PromotionCountryCode from a dict
promotion_country_code_from_dict = PromotionCountryCode.from_dict(promotion_country_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


