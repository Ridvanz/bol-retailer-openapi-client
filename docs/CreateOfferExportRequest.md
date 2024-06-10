# CreateOfferExportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** | The file format in which to return the export. | 

## Example

```python
from openapi_client.models.create_offer_export_request import CreateOfferExportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOfferExportRequest from a JSON string
create_offer_export_request_instance = CreateOfferExportRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOfferExportRequest.to_json())

# convert the object into a dict
create_offer_export_request_dict = create_offer_export_request_instance.to_dict()
# create an instance of CreateOfferExportRequest from a dict
create_offer_export_request_from_dict = CreateOfferExportRequest.from_dict(create_offer_export_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


