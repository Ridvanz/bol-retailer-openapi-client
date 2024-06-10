# AttributeValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The value of the attribute. | 
**unit_id** | **str** | The unit identifier of the attribute. | 

## Example

```python
from openapi_client.models.attribute_value import AttributeValue

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeValue from a JSON string
attribute_value_instance = AttributeValue.from_json(json)
# print the JSON string representation of the object
print(AttributeValue.to_json())

# convert the object into a dict
attribute_value_dict = attribute_value_instance.to_dict()
# create an instance of AttributeValue from a dict
attribute_value_from_dict = AttributeValue.from_dict(attribute_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


