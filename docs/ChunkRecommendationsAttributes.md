# ChunkRecommendationsAttributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**List[ChunkRecommendationsAttribute]**](ChunkRecommendationsAttribute.md) |  | 

## Example

```python
from openapi_client.models.chunk_recommendations_attributes import ChunkRecommendationsAttributes

# TODO update the JSON string below
json = "{}"
# create an instance of ChunkRecommendationsAttributes from a JSON string
chunk_recommendations_attributes_instance = ChunkRecommendationsAttributes.from_json(json)
# print the JSON string representation of the object
print(ChunkRecommendationsAttributes.to_json())

# convert the object into a dict
chunk_recommendations_attributes_dict = chunk_recommendations_attributes_instance.to_dict()
# create an instance of ChunkRecommendationsAttributes from a dict
chunk_recommendations_attributes_from_dict = ChunkRecommendationsAttributes.from_dict(chunk_recommendations_attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


