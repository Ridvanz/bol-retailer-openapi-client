# OfferInsights

Offer insights.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_insights** | [**List[OfferInsight]**](OfferInsight.md) |  | 

## Example

```python
from openapi_client.models.offer_insights import OfferInsights

# TODO update the JSON string below
json = "{}"
# create an instance of OfferInsights from a JSON string
offer_insights_instance = OfferInsights.from_json(json)
# print the JSON string representation of the object
print(OfferInsights.to_json())

# convert the object into a dict
offer_insights_dict = offer_insights_instance.to_dict()
# create an instance of OfferInsights from a dict
offer_insights_from_dict = OfferInsights.from_dict(offer_insights_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


