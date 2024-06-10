# RelevanceScore

The relevance score of a product in a promotion.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | The country for which the relevance score has been calculated against. | [optional] 
**relevance_score** | **int** | The calculated relevance score for the product. | [optional] 

## Example

```python
from openapi_client.models.relevance_score import RelevanceScore

# TODO update the JSON string below
json = "{}"
# create an instance of RelevanceScore from a JSON string
relevance_score_instance = RelevanceScore.from_json(json)
# print the JSON string representation of the object
print(RelevanceScore.to_json())

# convert the object into a dict
relevance_score_dict = relevance_score_instance.to_dict()
# create an instance of RelevanceScore from a dict
relevance_score_from_dict = RelevanceScore.from_dict(relevance_score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


