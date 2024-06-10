# OfferInsight


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the requested offer insight. | 
**type** | **str** | Interpretation of the data that applies to this measurement. | 
**total** | **float** | Total number of customer visits on the product page when the offer had the buy box over the requested period (excluding the current day). | [optional] 
**countries** | [**List[OfferInsightsCountry]**](OfferInsightsCountry.md) |  | 
**periods** | [**List[Periods]**](Periods.md) |  | 

## Example

```python
from openapi_client.models.offer_insight import OfferInsight

# TODO update the JSON string below
json = "{}"
# create an instance of OfferInsight from a JSON string
offer_insight_instance = OfferInsight.from_json(json)
# print the JSON string representation of the object
print(OfferInsight.to_json())

# convert the object into a dict
offer_insight_dict = offer_insight_instance.to_dict()
# create an instance of OfferInsight from a dict
offer_insight_from_dict = OfferInsight.from_dict(offer_insight_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


