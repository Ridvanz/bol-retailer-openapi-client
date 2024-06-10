# Attributes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identifier of the attribute. | 
**values** | [**List[Values]**](Values.md) |  | 

## Example

```python
from openapi_client.models.attributes import Attributes

# TODO update the JSON string below
json = "{}"
# create an instance of Attributes from a JSON string
attributes_instance = Attributes.from_json(json)
# print the JSON string representation of the object
print(Attributes.to_json())

# convert the object into a dict
attributes_dict = attributes_instance.to_dict()
# create an instance of Attributes from a dict
attributes_from_dict = Attributes.from_dict(attributes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


