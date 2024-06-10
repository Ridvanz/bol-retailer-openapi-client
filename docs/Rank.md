# Rank

The list of ranks associated with the product.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category_id** | **str** | The ID of the category to which the product belongs. | [optional] 
**search_term** | **str** | Search term related to the rank. | [optional] 
**was_sponsored** | **bool** | Indicator if the product is sponsored or not. | 
**rank** | **int** | The rank of the product in the category or search page. | 
**impressions** | **int** | Number of impressions of the product. | 

## Example

```python
from openapi_client.models.rank import Rank

# TODO update the JSON string below
json = "{}"
# create an instance of Rank from a JSON string
rank_instance = Rank.from_json(json)
# print the JSON string representation of the object
print(Rank.to_json())

# convert the object into a dict
rank_dict = rank_instance.to_dict()
# create an instance of Rank from a dict
rank_from_dict = Rank.from_dict(rank_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


