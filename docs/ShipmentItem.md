# ShipmentItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_item_id** | **str** | A unique identifier for the item of the order that was shipped in this shipment. | 
**fulfilment** | [**ShipmentFulfilment**](ShipmentFulfilment.md) |  | [optional] 
**offer** | [**OrderOffer**](OrderOffer.md) |  | [optional] 
**product** | [**OrderProduct**](OrderProduct.md) |  | [optional] 
**quantity** | **int** | Amount of the product being ordered. | 
**unit_price** | **float** | The selling price to the customer of a single unit including VAT. | 
**commission** | **float** | The commission. | [optional] 

## Example

```python
from openapi_client.models.shipment_item import ShipmentItem

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentItem from a JSON string
shipment_item_instance = ShipmentItem.from_json(json)
# print the JSON string representation of the object
print(ShipmentItem.to_json())

# convert the object into a dict
shipment_item_dict = shipment_item_instance.to_dict()
# create an instance of ShipmentItem from a dict
shipment_item_from_dict = ShipmentItem.from_dict(shipment_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


