# Fulfilment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** | The fulfilment method. Fulfilled by the retailer (FBR) or fulfilled by bol.com (FBB). | 
**delivery_code** | **str** | The delivery promise that applies to this offer. This value will only be used in combination with fulfilmentMethod &#39;FBR&#39;. | [optional] 

## Example

```python
from openapi_client.models.fulfilment import Fulfilment

# TODO update the JSON string below
json = "{}"
# create an instance of Fulfilment from a JSON string
fulfilment_instance = Fulfilment.from_json(json)
# print the JSON string representation of the object
print(Fulfilment.to_json())

# convert the object into a dict
fulfilment_dict = fulfilment_instance.to_dict()
# create an instance of Fulfilment from a dict
fulfilment_from_dict = Fulfilment.from_dict(fulfilment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


