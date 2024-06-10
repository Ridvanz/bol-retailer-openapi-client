# CommissionRange

Defines a specific price range for which the commission rates apply including VAT.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lower** | **float** | The inclusive lower price threshold for which the commission is valid. | 
**upper** | **float** | The exclusive upper price threshold for which the commission is valid. | [optional] 

## Example

```python
from openapi_client.models.commission_range import CommissionRange

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionRange from a JSON string
commission_range_instance = CommissionRange.from_json(json)
# print the JSON string representation of the object
print(CommissionRange.to_json())

# convert the object into a dict
commission_range_dict = commission_range_instance.to_dict()
# create an instance of CommissionRange from a dict
commission_range_from_dict = CommissionRange.from_dict(commission_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


