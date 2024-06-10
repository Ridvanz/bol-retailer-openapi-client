# ShippingLabelRequest

The configuration of order items to get delivery options for.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_items** | [**List[DeliveryOptionsRequestOrderItem]**](DeliveryOptionsRequestOrderItem.md) | Order items for which the delivery options are requested. | 
**shipping_label_offer_id** | **str** | Shipping label offer id for which you request a shipping label. | 

## Example

```python
from openapi_client.models.shipping_label_request import ShippingLabelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ShippingLabelRequest from a JSON string
shipping_label_request_instance = ShippingLabelRequest.from_json(json)
# print the JSON string representation of the object
print(ShippingLabelRequest.to_json())

# convert the object into a dict
shipping_label_request_dict = shipping_label_request_instance.to_dict()
# create an instance of ShippingLabelRequest from a dict
shipping_label_request_from_dict = ShippingLabelRequest.from_dict(shipping_label_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


