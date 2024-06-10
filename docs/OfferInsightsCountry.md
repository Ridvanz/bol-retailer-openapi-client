# OfferInsightsCountry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | Countries in which this offer is currently on sale in the webshop, in ISO-3166-1 format. | 
**value** | **float** | The total value of offer insight. | 

## Example

```python
from openapi_client.models.offer_insights_country import OfferInsightsCountry

# TODO update the JSON string below
json = "{}"
# create an instance of OfferInsightsCountry from a JSON string
offer_insights_country_instance = OfferInsightsCountry.from_json(json)
# print the JSON string representation of the object
print(OfferInsightsCountry.to_json())

# convert the object into a dict
offer_insights_country_dict = offer_insights_country_instance.to_dict()
# create an instance of OfferInsightsCountry from a dict
offer_insights_country_from_dict = OfferInsightsCountry.from_dict(offer_insights_country_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


