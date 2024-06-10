# InvalidReplenishmentLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Type of invalid replenishment line, in case the BSKU and/or EAN cannot be determined for this replenishment line. | 
**quantity_announced** | **int** | The amount of announced quantity for this replenishment line. | 
**quantity_received** | **int** | The amount of received quantity for this replenishment line. | 
**quantity_in_progress** | **int** | The amount of quantity that is still in progress at the warehouse for this replenishment line. | 
**quantity_with_graded_state** | **int** | The quantity within this shipment line that has a graded (unsalable) state. | 
**quantity_with_regular_state** | **int** | The quantity within this shipment line that has a regular (salable) state. | 

## Example

```python
from openapi_client.models.invalid_replenishment_line import InvalidReplenishmentLine

# TODO update the JSON string below
json = "{}"
# create an instance of InvalidReplenishmentLine from a JSON string
invalid_replenishment_line_instance = InvalidReplenishmentLine.from_json(json)
# print the JSON string representation of the object
print(InvalidReplenishmentLine.to_json())

# convert the object into a dict
invalid_replenishment_line_dict = invalid_replenishment_line_instance.to_dict()
# create an instance of InvalidReplenishmentLine from a dict
invalid_replenishment_line_from_dict = InvalidReplenishmentLine.from_dict(invalid_replenishment_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


