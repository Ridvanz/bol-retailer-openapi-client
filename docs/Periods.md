# Periods


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**period** | [**OfferInsightsPeriod**](OfferInsightsPeriod.md) |  | 
**total** | **float** | Total number of customer visits on the product page when the offer had the buy box over the requested period (excluding the current day). | [optional] 
**countries** | [**List[OfferInsightsCountry]**](OfferInsightsCountry.md) |  | [optional] 

## Example

```python
from openapi_client.models.periods import Periods

# TODO update the JSON string below
json = "{}"
# create an instance of Periods from a JSON string
periods_instance = Periods.from_json(json)
# print the JSON string representation of the object
print(Periods.to_json())

# convert the object into a dict
periods_dict = periods_instance.to_dict()
# create an instance of Periods from a dict
periods_from_dict = Periods.from_dict(periods_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


