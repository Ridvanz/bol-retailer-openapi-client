# ChunkRecommendationsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_contents** | [**List[ChunkRecommendationsAttributes]**](ChunkRecommendationsAttributes.md) |  | 

## Example

```python
from openapi_client.models.chunk_recommendations_request import ChunkRecommendationsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ChunkRecommendationsRequest from a JSON string
chunk_recommendations_request_instance = ChunkRecommendationsRequest.from_json(json)
# print the JSON string representation of the object
print(ChunkRecommendationsRequest.to_json())

# convert the object into a dict
chunk_recommendations_request_dict = chunk_recommendations_request_instance.to_dict()
# create an instance of ChunkRecommendationsRequest from a dict
chunk_recommendations_request_from_dict = ChunkRecommendationsRequest.from_dict(chunk_recommendations_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


