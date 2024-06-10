# UploadReportAttribute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identifier of the attribute for which the value has changed. | 
**values** | [**List[UploadReportValue]**](UploadReportValue.md) |  | 
**status** | **str** | The processing state of the submitted attribute. | 
**sub_status** | **str** | The reason code explaining why the value was rejected. | [optional] 
**sub_status_description** | **str** | The reason explaining why the value was rejected. | [optional] 

## Example

```python
from openapi_client.models.upload_report_attribute import UploadReportAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of UploadReportAttribute from a JSON string
upload_report_attribute_instance = UploadReportAttribute.from_json(json)
# print the JSON string representation of the object
print(UploadReportAttribute.to_json())

# convert the object into a dict
upload_report_attribute_dict = upload_report_attribute_instance.to_dict()
# create an instance of UploadReportAttribute from a dict
upload_report_attribute_from_dict = UploadReportAttribute.from_dict(upload_report_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


