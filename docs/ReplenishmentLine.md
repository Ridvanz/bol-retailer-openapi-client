# ReplenishmentLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ean** | **str** | The EAN number associated with this product. | 
**line_state** | **str** | The state of the line indicating whether this line was announced within this replenishment. | 
**quantity_announced** | **int** | The amount of announced quantity for this replenishment line. | 
**quantity_received** | **int** | The amount of received quantity for this replenishment line. | 
**quantity_in_progress** | **int** | The amount of quantity that is still in progress at the warehouse for this replenishment line. | 
**quantity_with_graded_state** | **int** | The quantity within this shipment line that has a graded (unsalable) state. | 
**quantity_with_regular_state** | **int** | The quantity within this shipment line that has a regular (salable) state. | 

## Example

```python
from openapi_client.models.replenishment_line import ReplenishmentLine

# TODO update the JSON string below
json = "{}"
# create an instance of ReplenishmentLine from a JSON string
replenishment_line_instance = ReplenishmentLine.from_json(json)
# print the JSON string representation of the object
print(ReplenishmentLine.to_json())

# convert the object into a dict
replenishment_line_dict = replenishment_line_instance.to_dict()
# create an instance of ReplenishmentLine from a dict
replenishment_line_from_dict = ReplenishmentLine.from_dict(replenishment_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


