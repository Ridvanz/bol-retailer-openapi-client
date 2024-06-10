# ReturnProcessingResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantity** | **int** | The processed quantity. | 
**processing_result** | **str** | The processing result of the return. | 
**handling_result** | **str** | The handling result requested by the retailer. | 
**processing_date_time** | **datetime** | The date and time in ISO 8601 format when the return was processed. | 

## Example

```python
from openapi_client.models.return_processing_result import ReturnProcessingResult

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnProcessingResult from a JSON string
return_processing_result_instance = ReturnProcessingResult.from_json(json)
# print the JSON string representation of the object
print(ReturnProcessingResult.to_json())

# convert the object into a dict
return_processing_result_dict = return_processing_result_instance.to_dict()
# create an instance of ReturnProcessingResult from a dict
return_processing_result_from_dict = ReturnProcessingResult.from_dict(return_processing_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


