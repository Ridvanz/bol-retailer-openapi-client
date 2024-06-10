# ReducedOrderItem

An order item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_item_id** | **str** | The id for the order item. One order can have multiple order items, but the list can only take one item. | 
**ean** | **str** | The EAN number associated with this product. | 
**fulfilment_method** | **str** | The fulfilment method. Fulfilled by the retailer (FBR) or fulfilled by bol.com (FBB). | 
**fulfilment_status** | **str** | To filter on order status. You can filter on either all orders independent from their status, open orders (excluding shipped and cancelled orders), and shipped orders. | 
**quantity** | **int** | Amount of ordered products for this order item id. | 
**quantity_shipped** | **int** | Amount of shipped products for this order item id. | 
**quantity_cancelled** | **int** | Amount of cancelled products for this order item id. | 
**cancellation_request** | **bool** | Indicates whether the order was cancelled on request of the customer before the retailer has shipped it. | 
**latest_changed_date_time** | **datetime** | The date and time in ISO 8601 format when the orderItem was last changed. | 

## Example

```python
from openapi_client.models.reduced_order_item import ReducedOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of ReducedOrderItem from a JSON string
reduced_order_item_instance = ReducedOrderItem.from_json(json)
# print the JSON string representation of the object
print(ReducedOrderItem.to_json())

# convert the object into a dict
reduced_order_item_dict = reduced_order_item_instance.to_dict()
# create an instance of ReducedOrderItem from a dict
reduced_order_item_from_dict = ReducedOrderItem.from_dict(reduced_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


