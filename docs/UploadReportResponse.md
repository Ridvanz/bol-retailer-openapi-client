# UploadReportResponse

Upload report.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upload_id** | **str** | The identifier of the upload report. | 
**language** | **str** | The language in which content is submitted. | 
**status** | **str** | The current status of the upload report. | 
**attributes** | [**List[UploadReportAttribute]**](UploadReportAttribute.md) |  | 
**assets** | [**List[UploadReportAsset]**](UploadReportAsset.md) |  | [optional] 

## Example

```python
from openapi_client.models.upload_report_response import UploadReportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UploadReportResponse from a JSON string
upload_report_response_instance = UploadReportResponse.from_json(json)
# print the JSON string representation of the object
print(UploadReportResponse.to_json())

# convert the object into a dict
upload_report_response_dict = upload_report_response_instance.to_dict()
# create an instance of UploadReportResponse from a dict
upload_report_response_from_dict = UploadReportResponse.from_dict(upload_report_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


