# ChunkRecommendationsPredictions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**predictions** | [**List[ChunkRecommendationsPrediction]**](ChunkRecommendationsPrediction.md) |  | 

## Example

```python
from openapi_client.models.chunk_recommendations_predictions import ChunkRecommendationsPredictions

# TODO update the JSON string below
json = "{}"
# create an instance of ChunkRecommendationsPredictions from a JSON string
chunk_recommendations_predictions_instance = ChunkRecommendationsPredictions.from_json(json)
# print the JSON string representation of the object
print(ChunkRecommendationsPredictions.to_json())

# convert the object into a dict
chunk_recommendations_predictions_dict = chunk_recommendations_predictions_instance.to_dict()
# create an instance of ChunkRecommendationsPredictions from a dict
chunk_recommendations_predictions_from_dict = ChunkRecommendationsPredictions.from_dict(chunk_recommendations_predictions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


