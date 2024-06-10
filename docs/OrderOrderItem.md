# OrderOrderItem

Order item details from an order.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_item_id** | **str** | The id for the order item. One order can have multiple order items, but the list can only take one item. | 
**cancellation_request** | **bool** | Indicates whether the order was cancelled on request of the customer before the retailer has shipped it. | 
**fulfilment** | [**OrderFulfilment**](OrderFulfilment.md) |  | [optional] 
**offer** | [**OrderOffer**](OrderOffer.md) |  | [optional] 
**product** | [**OrderProduct**](OrderProduct.md) |  | [optional] 
**quantity** | **int** | Amount of ordered products for this order item id. | 
**quantity_shipped** | **int** | Amount of shipped products for this order item id. | 
**quantity_cancelled** | **int** | Amount of cancelled products for this order item id. | 
**unit_price** | **float** | The selling price to the customer of a single unit including VAT. | 
**commission** | **float** | The commission for all quantities of this order item. | 
**additional_services** | [**List[AdditionalService]**](AdditionalService.md) |  | [optional] 
**latest_changed_date_time** | **datetime** | The date and time in ISO 8601 format when the orderItem was last changed. | 

## Example

```python
from openapi_client.models.order_order_item import OrderOrderItem

# TODO update the JSON string below
json = "{}"
# create an instance of OrderOrderItem from a JSON string
order_order_item_instance = OrderOrderItem.from_json(json)
# print the JSON string representation of the object
print(OrderOrderItem.to_json())

# convert the object into a dict
order_order_item_dict = order_order_item_instance.to_dict()
# create an instance of OrderOrderItem from a dict
order_order_item_from_dict = OrderOrderItem.from_dict(order_order_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


