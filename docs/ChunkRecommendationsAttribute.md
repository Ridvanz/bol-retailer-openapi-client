# ChunkRecommendationsAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identifier of the attribute. | 
**values** | [**List[ChunkRecommendationsValue]**](ChunkRecommendationsValue.md) |  | 

## Example

```python
from openapi_client.models.chunk_recommendations_attribute import ChunkRecommendationsAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of ChunkRecommendationsAttribute from a JSON string
chunk_recommendations_attribute_instance = ChunkRecommendationsAttribute.from_json(json)
# print the JSON string representation of the object
print(ChunkRecommendationsAttribute.to_json())

# convert the object into a dict
chunk_recommendations_attribute_dict = chunk_recommendations_attribute_instance.to_dict()
# create an instance of ChunkRecommendationsAttribute from a dict
chunk_recommendations_attribute_from_dict = ChunkRecommendationsAttribute.from_dict(chunk_recommendations_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


