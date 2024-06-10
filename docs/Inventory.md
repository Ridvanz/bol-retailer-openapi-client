# Inventory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ean** | **str** | The EAN number associated with this product. | 
**bsku** | **str** | The BSKU number associated with this product. | 
**graded_stock** | **int** | The stock that is not available for sale anymore. | 
**regular_stock** | **int** | The stock that is available for sale. | 
**title** | **str** | The product title. | 

## Example

```python
from openapi_client.models.inventory import Inventory

# TODO update the JSON string below
json = "{}"
# create an instance of Inventory from a JSON string
inventory_instance = Inventory.from_json(json)
# print the JSON string representation of the object
print(Inventory.to_json())

# convert the object into a dict
inventory_dict = inventory_instance.to_dict()
# create an instance of Inventory from a dict
inventory_from_dict = Inventory.from_dict(inventory_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


