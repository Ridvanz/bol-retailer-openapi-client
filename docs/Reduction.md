# Reduction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maximum_price** | **float** | Maximum offer price that can be used to benefit from a commission reduction, including VAT. | 
**cost_reduction** | **float** | A reduction to the commission if the maximum price criteria is met, including VAT. | 
**start_date** | **date** | The start date from which the commission reduction is valid, in ISO 8601 format. | 
**end_date** | **date** | The end date from which the commission reduction is not valid anymore, in ISO 8601 format. | 

## Example

```python
from openapi_client.models.reduction import Reduction

# TODO update the JSON string below
json = "{}"
# create an instance of Reduction from a JSON string
reduction_instance = Reduction.from_json(json)
# print the JSON string representation of the object
print(Reduction.to_json())

# convert the object into a dict
reduction_dict = reduction_instance.to_dict()
# create an instance of Reduction from a dict
reduction_from_dict = Reduction.from_dict(reduction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


