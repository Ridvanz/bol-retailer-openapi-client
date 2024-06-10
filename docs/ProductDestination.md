# ProductDestination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_warehouse** | [**ProductDestinationWarehouse**](ProductDestinationWarehouse.md) |  | 
**eans** | [**List[Ean]**](Ean.md) |  | 

## Example

```python
from openapi_client.models.product_destination import ProductDestination

# TODO update the JSON string below
json = "{}"
# create an instance of ProductDestination from a JSON string
product_destination_instance = ProductDestination.from_json(json)
# print the JSON string representation of the object
print(ProductDestination.to_json())

# convert the object into a dict
product_destination_dict = product_destination_instance.to_dict()
# create an instance of ProductDestination from a dict
product_destination_from_dict = ProductDestination.from_dict(product_destination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


