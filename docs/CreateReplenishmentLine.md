# CreateReplenishmentLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ean** | **str** | The EAN number associated with this product. | 
**quantity** | **int** | The number of announced items. | 

## Example

```python
from openapi_client.models.create_replenishment_line import CreateReplenishmentLine

# TODO update the JSON string below
json = "{}"
# create an instance of CreateReplenishmentLine from a JSON string
create_replenishment_line_instance = CreateReplenishmentLine.from_json(json)
# print the JSON string representation of the object
print(CreateReplenishmentLine.to_json())

# convert the object into a dict
create_replenishment_line_dict = create_replenishment_line_instance.to_dict()
# create an instance of CreateReplenishmentLine from a dict
create_replenishment_line_from_dict = CreateReplenishmentLine.from_dict(create_replenishment_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


