# ReturnReason

The reason why the customer returned this product.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**main_reason** | **str** | The main reason describing why the customer returned this product. | 
**detailed_reason** | **str** | The sub reason describing why the customer returned this product in more detail. | [optional] 
**customer_comments** | **str** | Additional details from the customer as to why this item was returned. | 

## Example

```python
from openapi_client.models.return_reason import ReturnReason

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnReason from a JSON string
return_reason_instance = ReturnReason.from_json(json)
# print the JSON string representation of the object
print(ReturnReason.to_json())

# convert the object into a dict
return_reason_dict = return_reason_instance.to_dict()
# create an instance of ReturnReason from a dict
return_reason_from_dict = ReturnReason.from_dict(return_reason_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


