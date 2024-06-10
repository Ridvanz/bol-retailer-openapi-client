# SalesForecastResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Indicator name. | 
**type** | **str** | Interpretation of the data that applies to this measurement. | 
**total** | [**Total**](Total.md) |  | 
**countries** | [**List[Countries]**](Countries.md) |  | 
**periods** | [**List[SalesForecastPeriod]**](SalesForecastPeriod.md) |  | 

## Example

```python
from openapi_client.models.sales_forecast_response import SalesForecastResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SalesForecastResponse from a JSON string
sales_forecast_response_instance = SalesForecastResponse.from_json(json)
# print the JSON string representation of the object
print(SalesForecastResponse.to_json())

# convert the object into a dict
sales_forecast_response_dict = sales_forecast_response_instance.to_dict()
# create an instance of SalesForecastResponse from a dict
sales_forecast_response_from_dict = SalesForecastResponse.from_dict(sales_forecast_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


