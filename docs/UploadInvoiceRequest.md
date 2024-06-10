# UploadInvoiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invoice** | **bytearray** | The invoice file. | 

## Example

```python
from openapi_client.models.upload_invoice_request import UploadInvoiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UploadInvoiceRequest from a JSON string
upload_invoice_request_instance = UploadInvoiceRequest.from_json(json)
# print the JSON string representation of the object
print(UploadInvoiceRequest.to_json())

# convert the object into a dict
upload_invoice_request_dict = upload_invoice_request_instance.to_dict()
# create an instance of UploadInvoiceRequest from a dict
upload_invoice_request_from_dict = UploadInvoiceRequest.from_dict(upload_invoice_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


