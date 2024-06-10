# OrderProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ean** | **str** | The EAN number associated with this product. | 
**title** | **str** | Title of the product as shown on the webshop. | 

## Example

```python
from openapi_client.models.order_product import OrderProduct

# TODO update the JSON string below
json = "{}"
# create an instance of OrderProduct from a JSON string
order_product_instance = OrderProduct.from_json(json)
# print the JSON string representation of the object
print(OrderProduct.to_json())

# convert the object into a dict
order_product_dict = order_product_instance.to_dict()
# create an instance of OrderProduct from a dict
order_product_from_dict = OrderProduct.from_dict(order_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


