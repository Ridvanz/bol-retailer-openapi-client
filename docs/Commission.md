# Commission


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ean** | **str** | The EAN number associated with this product. | 
**condition** | **str** | The condition of the offer. | 
**unit_price** | **float** | The intended selling price per single unit up to 2 decimals precision, including VAT. | 
**fixed_amount** | **float** | A fixed commission fee, including VAT. | 
**percentage** | **float** | A percentage of commission, based on the intended selling price per unit, including VAT. | 
**total_cost** | **float** | The total commission for selling this product at bol.com. The price includes VAT for Dutch sellers, and excludes VAT for Belgium sellers. | 
**total_cost_without_reduction** | **float** | The total commission for selling this product at bol.com without reductions including VAT. | [optional] 
**reductions** | [**List[Reduction]**](Reduction.md) |  | 

## Example

```python
from openapi_client.models.commission import Commission

# TODO update the JSON string below
json = "{}"
# create an instance of Commission from a JSON string
commission_instance = Commission.from_json(json)
# print the JSON string representation of the object
print(Commission.to_json())

# convert the object into a dict
commission_dict = commission_instance.to_dict()
# create an instance of Commission from a dict
commission_from_dict = Commission.from_dict(commission_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


