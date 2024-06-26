# Stock


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | The amount of stock available for the specified product present in the retailers warehouse. Note: this should not be the FBB stock! Defaults to 0. | [optional] 
**corrected_stock** | **int** | The amount of order items in stock minus handled order items and minus open order items. As compared to the stock you sent us. When this reaches 0, your offer will not be for sale on the shop. | [optional] 
**managed_by_retailer** | **bool** | Configures whether the retailer manages the stock levels or that bol.com should calculate the corrected stock based on actual open orders. In case the configuration is set to &#39;false&#39;, all open orders are used to calculate the corrected stock. In case the configuration is set to &#39;true&#39;, only orders that are placed after the last offer update are taken into account. | 

## Example

```python
from openapi_client.models.stock import Stock

# TODO update the JSON string below
json = "{}"
# create an instance of Stock from a JSON string
stock_instance = Stock.from_json(json)
# print the JSON string representation of the object
print(Stock.to_json())

# convert the object into a dict
stock_dict = stock_instance.to_dict()
# create an instance of Stock from a dict
stock_from_dict = Stock.from_dict(stock_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


