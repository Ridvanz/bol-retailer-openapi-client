# ReducedInvalidReplenishmentLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of invalid replenishment line, in case the BSKU and/or EAN cannot be determined for this replenishment line. | 

## Example

```python
from openapi_client.models.reduced_invalid_replenishment_line import ReducedInvalidReplenishmentLine

# TODO update the JSON string below
json = "{}"
# create an instance of ReducedInvalidReplenishmentLine from a JSON string
reduced_invalid_replenishment_line_instance = ReducedInvalidReplenishmentLine.from_json(json)
# print the JSON string representation of the object
print(ReducedInvalidReplenishmentLine.to_json())

# convert the object into a dict
reduced_invalid_replenishment_line_dict = reduced_invalid_replenishment_line_instance.to_dict()
# create an instance of ReducedInvalidReplenishmentLine from a dict
reduced_invalid_replenishment_line_from_dict = ReducedInvalidReplenishmentLine.from_dict(reduced_invalid_replenishment_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


