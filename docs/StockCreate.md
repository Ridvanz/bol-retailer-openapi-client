# StockCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | The amount of stock available for the specified product present in the retailers warehouse. Note: this should not be the FBB stock! Defaults to 0. | 
**managed_by_retailer** | **bool** | Configures whether the retailer manages the stock levels or that bol.com should calculate the corrected stock based on actual open orders. In case the configuration is set to &#39;false&#39;, all open orders are used to calculate the corrected stock. In case the configuration is set to &#39;true&#39;, only orders that are placed after the last offer update are taken into account. | 

## Example

```python
from openapi_client.models.stock_create import StockCreate

# TODO update the JSON string below
json = "{}"
# create an instance of StockCreate from a JSON string
stock_create_instance = StockCreate.from_json(json)
# print the JSON string representation of the object
print(StockCreate.to_json())

# convert the object into a dict
stock_create_dict = stock_create_instance.to_dict()
# create an instance of StockCreate from a dict
stock_create_from_dict = StockCreate.from_dict(stock_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


