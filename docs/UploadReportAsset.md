# UploadReportAsset


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL of the asset. | 
**labels** | **List[str]** | The label(s) of the asset. | 
**status** | **str** | The processing state of the submitted asset. | 
**sub_status** | **str** | The reason code explaining why the value was rejected. | [optional] 
**sub_status_description** | **str** | The reason explaining why the value was rejected. | [optional] 

## Example

```python
from openapi_client.models.upload_report_asset import UploadReportAsset

# TODO update the JSON string below
json = "{}"
# create an instance of UploadReportAsset from a JSON string
upload_report_asset_instance = UploadReportAsset.from_json(json)
# print the JSON string representation of the object
print(UploadReportAsset.to_json())

# convert the object into a dict
upload_report_asset_dict = upload_report_asset_instance.to_dict()
# create an instance of UploadReportAsset from a dict
upload_report_asset_from_dict = UploadReportAsset.from_dict(upload_report_asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


