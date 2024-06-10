# CommissionRate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ean** | **str** | The EAN number associated with this product. | 
**date_ranges** | [**List[CommissionDateRange]**](CommissionDateRange.md) | An array of objects, each describing a period during which certain commission rates apply. | 

## Example

```python
from openapi_client.models.commission_rate import CommissionRate

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionRate from a JSON string
commission_rate_instance = CommissionRate.from_json(json)
# print the JSON string representation of the object
print(CommissionRate.to_json())

# convert the object into a dict
commission_rate_dict = commission_rate_instance.to_dict()
# create an instance of CommissionRate from a dict
commission_rate_from_dict = CommissionRate.from_dict(commission_rate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


