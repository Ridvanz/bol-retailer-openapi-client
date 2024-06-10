# Serie


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the product serie(s) the EAN belongs to. | [optional] 

## Example

```python
from openapi_client.models.serie import Serie

# TODO update the JSON string below
json = "{}"
# create an instance of Serie from a JSON string
serie_instance = Serie.from_json(json)
# print the JSON string representation of the object
print(Serie.to_json())

# convert the object into a dict
serie_dict = serie_instance.to_dict()
# create an instance of Serie from a dict
serie_from_dict = Serie.from_dict(serie_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


