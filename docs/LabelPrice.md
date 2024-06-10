# LabelPrice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_price** | **float** | The price that is charged for this delivery option, excluding VAT. | 

## Example

```python
from openapi_client.models.label_price import LabelPrice

# TODO update the JSON string below
json = "{}"
# create an instance of LabelPrice from a JSON string
label_price_instance = LabelPrice.from_json(json)
# print the JSON string representation of the object
print(LabelPrice.to_json())

# convert the object into a dict
label_price_dict = label_price_instance.to_dict()
# create an instance of LabelPrice from a dict
label_price_from_dict = LabelPrice.from_dict(label_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


