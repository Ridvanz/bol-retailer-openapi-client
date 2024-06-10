# PriceStarBoundaryLevels


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**level** | **int** | The level of the price star boundary. | 
**boundary_price** | **float** | The boundary price of the corresponding level. | 

## Example

```python
from openapi_client.models.price_star_boundary_levels import PriceStarBoundaryLevels

# TODO update the JSON string below
json = "{}"
# create an instance of PriceStarBoundaryLevels from a JSON string
price_star_boundary_levels_instance = PriceStarBoundaryLevels.from_json(json)
# print the JSON string representation of the object
print(PriceStarBoundaryLevels.to_json())

# convert the object into a dict
price_star_boundary_levels_dict = price_star_boundary_levels_instance.to_dict()
# create an instance of PriceStarBoundaryLevels from a dict
price_star_boundary_levels_from_dict = PriceStarBoundaryLevels.from_dict(price_star_boundary_levels_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


