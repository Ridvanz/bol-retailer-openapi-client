# UpdateOfferStockRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | The amount of stock available for the specified product present in the retailers warehouse. Note: this should not be the FBB stock! Defaults to 0. | 
**managed_by_retailer** | **bool** | Configures whether the retailer manages the stock levels or that bol.com should calculate the corrected stock based on actual open orders. In case the configuration is set to &#39;false&#39;, all open orders are used to calculate the corrected stock. In case the configuration is set to &#39;true&#39;, only orders that are placed after the last offer update are taken into account. | 

## Example

```python
from openapi_client.models.update_offer_stock_request import UpdateOfferStockRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOfferStockRequest from a JSON string
update_offer_stock_request_instance = UpdateOfferStockRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateOfferStockRequest.to_json())

# convert the object into a dict
update_offer_stock_request_dict = update_offer_stock_request_instance.to_dict()
# create an instance of UpdateOfferStockRequest from a dict
update_offer_stock_request_from_dict = UpdateOfferStockRequest.from_dict(update_offer_stock_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


