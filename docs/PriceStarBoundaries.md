# PriceStarBoundaries


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_modified_date_time** | **datetime** | The date and time in ISO 8601 format when boundaries updated for the last time. | 
**price_star_boundary_levels** | [**List[PriceStarBoundaryLevels]**](PriceStarBoundaryLevels.md) |  | 

## Example

```python
from openapi_client.models.price_star_boundaries import PriceStarBoundaries

# TODO update the JSON string below
json = "{}"
# create an instance of PriceStarBoundaries from a JSON string
price_star_boundaries_instance = PriceStarBoundaries.from_json(json)
# print the JSON string representation of the object
print(PriceStarBoundaries.to_json())

# convert the object into a dict
price_star_boundaries_dict = price_star_boundaries_instance.to_dict()
# create an instance of PriceStarBoundaries from a dict
price_star_boundaries_from_dict = PriceStarBoundaries.from_dict(price_star_boundaries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


