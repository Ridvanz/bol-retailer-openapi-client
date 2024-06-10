# CreateProductContentSingleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | The language in which content is submitted. | 
**attributes** | [**List[Attribute]**](Attribute.md) | A list of attributes. Every content update request should have one \&quot;EAN\&quot; attribute to link changes to a proper product. | 
**assets** | [**List[Asset]**](Asset.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_product_content_single_request import CreateProductContentSingleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProductContentSingleRequest from a JSON string
create_product_content_single_request_instance = CreateProductContentSingleRequest.from_json(json)
# print the JSON string representation of the object
print(CreateProductContentSingleRequest.to_json())

# convert the object into a dict
create_product_content_single_request_dict = create_product_content_single_request_instance.to_dict()
# create an instance of CreateProductContentSingleRequest from a dict
create_product_content_single_request_from_dict = CreateProductContentSingleRequest.from_dict(create_product_content_single_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


