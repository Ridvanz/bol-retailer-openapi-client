# ChunkRecommendationsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recommendations** | [**List[ChunkRecommendationsPredictions]**](ChunkRecommendationsPredictions.md) |  | 

## Example

```python
from openapi_client.models.chunk_recommendations_response import ChunkRecommendationsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChunkRecommendationsResponse from a JSON string
chunk_recommendations_response_instance = ChunkRecommendationsResponse.from_json(json)
# print the JSON string representation of the object
print(ChunkRecommendationsResponse.to_json())

# convert the object into a dict
chunk_recommendations_response_dict = chunk_recommendations_response_instance.to_dict()
# create an instance of ChunkRecommendationsResponse from a dict
chunk_recommendations_response_from_dict = ChunkRecommendationsResponse.from_dict(chunk_recommendations_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


