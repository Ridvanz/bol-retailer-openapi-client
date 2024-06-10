# CommissionProducts


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products** | [**List[Ean]**](Ean.md) |  | 

## Example

```python
from openapi_client.models.commission_products import CommissionProducts

# TODO update the JSON string below
json = "{}"
# create an instance of CommissionProducts from a JSON string
commission_products_instance = CommissionProducts.from_json(json)
# print the JSON string representation of the object
print(CommissionProducts.to_json())

# convert the object into a dict
commission_products_dict = commission_products_instance.to_dict()
# create an instance of CommissionProducts from a dict
commission_products_from_dict = CommissionProducts.from_dict(commission_products_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


