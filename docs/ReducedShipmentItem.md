# ReducedShipmentItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_item_id** | **str** | A unique identifier for the item of the order that was shipped in this shipment. | 
**ean** | **str** | The EAN number associated with this product. | 

## Example

```python
from openapi_client.models.reduced_shipment_item import ReducedShipmentItem

# TODO update the JSON string below
json = "{}"
# create an instance of ReducedShipmentItem from a JSON string
reduced_shipment_item_instance = ReducedShipmentItem.from_json(json)
# print the JSON string representation of the object
print(ReducedShipmentItem.to_json())

# convert the object into a dict
reduced_shipment_item_dict = reduced_shipment_item_instance.to_dict()
# create an instance of ReducedShipmentItem from a dict
reduced_shipment_item_from_dict = ReducedShipmentItem.from_dict(reduced_shipment_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


