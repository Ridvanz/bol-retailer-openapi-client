# SalesForecastPeriod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**weeks_ahead** | **int** | The number of weeks into the future, starting from today. | 
**total** | [**Total**](Total.md) |  | 
**countries** | [**List[Countries]**](Countries.md) |  | 

## Example

```python
from openapi_client.models.sales_forecast_period import SalesForecastPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of SalesForecastPeriod from a JSON string
sales_forecast_period_instance = SalesForecastPeriod.from_json(json)
# print the JSON string representation of the object
print(SalesForecastPeriod.to_json())

# convert the object into a dict
sales_forecast_period_dict = sales_forecast_period_instance.to_dict()
# create an instance of SalesForecastPeriod from a dict
sales_forecast_period_from_dict = SalesForecastPeriod.from_dict(sales_forecast_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


