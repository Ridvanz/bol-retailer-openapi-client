# ShipmentsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipments** | [**List[ReducedShipment]**](ReducedShipment.md) |  | 

## Example

```python
from openapi_client.models.shipments_response import ShipmentsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentsResponse from a JSON string
shipments_response_instance = ShipmentsResponse.from_json(json)
# print the JSON string representation of the object
print(ShipmentsResponse.to_json())

# convert the object into a dict
shipments_response_dict = shipments_response_instance.to_dict()
# create an instance of ShipmentsResponse from a dict
shipments_response_from_dict = ShipmentsResponse.from_dict(shipments_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


