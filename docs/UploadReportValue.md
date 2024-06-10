# UploadReportValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The value of the attribute. | 
**unit_id** | **str** | The unit identifier of the attribute. | [optional] 

## Example

```python
from openapi_client.models.upload_report_value import UploadReportValue

# TODO update the JSON string below
json = "{}"
# create an instance of UploadReportValue from a JSON string
upload_report_value_instance = UploadReportValue.from_json(json)
# print the JSON string representation of the object
print(UploadReportValue.to_json())

# convert the object into a dict
upload_report_value_dict = upload_report_value_instance.to_dict()
# create an instance of UploadReportValue from a dict
upload_report_value_from_dict = UploadReportValue.from_dict(upload_report_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


