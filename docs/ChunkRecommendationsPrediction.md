# ChunkRecommendationsPrediction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chunk_id** | **str** | The identifier of the predicted GPC/Product Classification. | 
**probability** | **float** | The probability of the predicted chunk as a ratio, with eleven decimals of precision. | 

## Example

```python
from openapi_client.models.chunk_recommendations_prediction import ChunkRecommendationsPrediction

# TODO update the JSON string below
json = "{}"
# create an instance of ChunkRecommendationsPrediction from a JSON string
chunk_recommendations_prediction_instance = ChunkRecommendationsPrediction.from_json(json)
# print the JSON string representation of the object
print(ChunkRecommendationsPrediction.to_json())

# convert the object into a dict
chunk_recommendations_prediction_dict = chunk_recommendations_prediction_instance.to_dict()
# create an instance of ChunkRecommendationsPrediction from a dict
chunk_recommendations_prediction_from_dict = ChunkRecommendationsPrediction.from_dict(chunk_recommendations_prediction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


