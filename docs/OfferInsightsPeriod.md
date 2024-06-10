# OfferInsightsPeriod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | **int** | Day of the month. | [optional] 
**week** | **int** | Week of the year. | [optional] 
**month** | **int** | Month of the year. | [optional] 
**year** | **int** | Year. | 

## Example

```python
from openapi_client.models.offer_insights_period import OfferInsightsPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of OfferInsightsPeriod from a JSON string
offer_insights_period_instance = OfferInsightsPeriod.from_json(json)
# print the JSON string representation of the object
print(OfferInsightsPeriod.to_json())

# convert the object into a dict
offer_insights_period_dict = offer_insights_period_instance.to_dict()
# create an instance of OfferInsightsPeriod from a dict
offer_insights_period_from_dict = OfferInsightsPeriod.from_dict(offer_insights_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


