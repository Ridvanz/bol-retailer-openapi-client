# CommissionDateRange

An array of objects, each describing a period during which certain commission rates apply.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_date** | **str** | The inclusive start date (in ISO 8601 format) from which the commission applies | 
**end_date** | **str** | The exclusive end date (in ISO 8601 format) after which the commission no longer applies. | 
**rates** | [**List[CommissionDateRate]**](CommissionDateRate.md) | An array of objects, each describing commission rates for a specific condition. | 

## Example

```python
from openapi_client.models.commission_date_range import CommissionDateRange

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionDateRange from a JSON string
commission_date_range_instance = CommissionDateRange.from_json(json)
# print the JSON string representation of the object
print(CommissionDateRange.to_json())

# convert the object into a dict
commission_date_range_dict = commission_date_range_instance.to_dict()
# create an instance of CommissionDateRange from a dict
commission_date_range_from_dict = CommissionDateRange.from_dict(commission_date_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


