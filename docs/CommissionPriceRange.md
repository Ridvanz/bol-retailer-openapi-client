# CommissionPriceRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**range** | [**CommissionRange**](CommissionRange.md) |  | 
**fixed_amount** | **float** | The fixed commission amount excluding VAT. | 
**percentage** | **float** | A percentage of commission, based on the intended selling price per unit, excluding VAT. | 
**reduction_applied** | **bool** | A boolean flag indicating whether a reduction is applied to the commission or not. | 

## Example

```python
from openapi_client.models.commission_price_range import CommissionPriceRange

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionPriceRange from a JSON string
commission_price_range_instance = CommissionPriceRange.from_json(json)
# print the JSON string representation of the object
print(CommissionPriceRange.to_json())

# convert the object into a dict
commission_price_range_dict = commission_price_range_instance.to_dict()
# create an instance of CommissionPriceRange from a dict
commission_price_range_from_dict = CommissionPriceRange.from_dict(commission_price_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


