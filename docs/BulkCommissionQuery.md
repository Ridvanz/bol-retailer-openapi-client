# BulkCommissionQuery


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ean** | **str** | The EAN number associated with this product. | 
**condition** | **str** | The condition of the offer. | [optional] 
**unit_price** | **float** | The price of the product with a period as a decimal separator. The price should always have two decimals precision. | 

## Example

```python
from openapi_client.models.bulk_commission_query import BulkCommissionQuery

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCommissionQuery from a JSON string
bulk_commission_query_instance = BulkCommissionQuery.from_json(json)
# print the JSON string representation of the object
print(BulkCommissionQuery.to_json())

# convert the object into a dict
bulk_commission_query_dict = bulk_commission_query_instance.to_dict()
# create an instance of BulkCommissionQuery from a dict
bulk_commission_query_from_dict = BulkCommissionQuery.from_dict(bulk_commission_query_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


