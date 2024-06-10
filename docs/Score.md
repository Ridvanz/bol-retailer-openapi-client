# Score

The score for this measurement. In case there are no scores for an indicator, this element is omitted from the response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conforms** | **bool** | Indicates whether the score conforms to the bol.com service norm or not. | 
**numerator** | **int** | The top part of the fraction (above the line). This usually is the smaller number compared to the denominator. | 
**denominator** | **int** | The lower part of the fraction (below the line). This usually is the larger number compared to the the numerator. | 
**value** | **float** | The score for this measurement (denominator divided by the numerator). | 
**distance_to_norm** | **float** | The difference between the score and the bol.com service norm. | 

## Example

```python
from openapi_client.models.score import Score

# TODO update the JSON string below
json = "{}"
# create an instance of Score from a JSON string
score_instance = Score.from_json(json)
# print the JSON string representation of the object
print(Score.to_json())

# convert the object into a dict
score_dict = score_instance.to_dict()
# create an instance of Score from a dict
score_from_dict = Score.from_dict(score_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


