# ShipmentFulfilment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**method** | **str** | The fulfilment method. Fulfilled by the retailer (FBR) or fulfilled by bol.com (FBB). | 
**distribution_party** | **str** | The party that manages the distribution, either bol.com or the retailer itself. | [optional] 
**latest_delivery_date** | **date** | The ultimate delivery date at which this order must be delivered at the customer&#39;s shipping address. This field is empty in case the exactDeliveryDate is filled. | [optional] 

## Example

```python
from openapi_client.models.shipment_fulfilment import ShipmentFulfilment

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentFulfilment from a JSON string
shipment_fulfilment_instance = ShipmentFulfilment.from_json(json)
# print the JSON string representation of the object
print(ShipmentFulfilment.to_json())

# convert the object into a dict
shipment_fulfilment_dict = shipment_fulfilment_instance.to_dict()
# create an instance of ShipmentFulfilment from a dict
shipment_fulfilment_from_dict = ShipmentFulfilment.from_dict(shipment_fulfilment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


