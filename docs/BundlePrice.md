# BundlePrice

A set of prices (containing a quantity and selling price) that apply to this offer.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **int** | The minimum quantity a customer must order in order to receive discount. The element with value 1 must at least be present. In case of using more elements, the respective quantities must be in increasing order. | 
**unit_price** | **float** | The price per single unit including VAT in case the customer orders at least the quantity provided. When using more than 1 price, the respective prices must be in decreasing order using 2 decimal precision and dot separated. | 

## Example

```python
from openapi_client.models.bundle_price import BundlePrice

# TODO update the JSON string below
json = "{}"
# create an instance of BundlePrice from a JSON string
bundle_price_instance = BundlePrice.from_json(json)
# print the JSON string representation of the object
print(BundlePrice.to_json())

# convert the object into a dict
bundle_price_dict = bundle_price_instance.to_dict()
# create an instance of BundlePrice from a dict
bundle_price_from_dict = BundlePrice.from_dict(bundle_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


