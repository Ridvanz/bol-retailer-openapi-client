# ProductRanks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ranks** | [**List[Rank]**](Rank.md) | The list of ranks associated with the product. | 
**has_next_page** | **bool** | Indicator if there is a next page of ranks (true/false). | 

## Example

```python
from openapi_client.models.product_ranks import ProductRanks

# TODO update the JSON string below
json = "{}"
# create an instance of ProductRanks from a JSON string
product_ranks_instance = ProductRanks.from_json(json)
# print the JSON string representation of the object
print(ProductRanks.to_json())

# convert the object into a dict
product_ranks_dict = product_ranks_instance.to_dict()
# create an instance of ProductRanks from a dict
product_ranks_from_dict = ProductRanks.from_dict(product_ranks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


