# CommissionDateRate

An array of objects, each describing commission rates for a specific condition.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**condition** | **str** | Condition of the product. | 
**price_ranges** | [**List[CommissionPriceRange]**](CommissionPriceRange.md) |  | 

## Example

```python
from openapi_client.models.commission_date_rate import CommissionDateRate

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionDateRate from a JSON string
commission_date_rate_instance = CommissionDateRate.from_json(json)
# print the JSON string representation of the object
print(CommissionDateRate.to_json())

# convert the object into a dict
commission_date_rate_dict = commission_date_rate_instance.to_dict()
# create an instance of CommissionDateRate from a dict
commission_date_rate_from_dict = CommissionDateRate.from_dict(commission_date_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


