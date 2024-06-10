# OrderFulfilment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** | The fulfilment method. Fulfilled by the retailer (FBR) or fulfilled by bol.com (FBB). | 
**distribution_party** | **str** | The party that manages the distribution, either bol.com or the retailer itself. | [optional] 
**latest_delivery_date** | **date** | The ultimate delivery date at which this order must be delivered at the customer&#39;s shipping address. This field is empty in case the exactDeliveryDate is filled. | [optional] 
**exact_delivery_date** | **date** | The exact delivery date at which this order must be delivered at the customer&#39;s shipping address. This field is only filled when the customer chose an exact date for delivery. This field is empty in case the latestDeliveryDate is filled. | [optional] 
**expiry_date** | **date** | The date this order item will automatically expire and thereby cancelling this order item from the order. | [optional] 
**time_frame_type** | **str** | Delivery option selected by the customer. | 

## Example

```python
from openapi_client.models.order_fulfilment import OrderFulfilment

# TODO update the JSON string below
json = "{}"
# create an instance of OrderFulfilment from a JSON string
order_fulfilment_instance = OrderFulfilment.from_json(json)
# print the JSON string representation of the object
print(OrderFulfilment.to_json())

# convert the object into a dict
order_fulfilment_dict = order_fulfilment_instance.to_dict()
# create an instance of OrderFulfilment from a dict
order_fulfilment_from_dict = OrderFulfilment.from_dict(order_fulfilment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


