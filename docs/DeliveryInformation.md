# DeliveryInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected_delivery_date** | **date** | The expected delivery date of the shipment at the bol.com warehouse in ISO 8601 format. | 
**transporter_code** | **str** | The transporter that will pickup this replenishment. | 
**destination_warehouse** | [**DestinationWarehouse**](DestinationWarehouse.md) |  | 

## Example

```python
from openapi_client.models.delivery_information import DeliveryInformation

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryInformation from a JSON string
delivery_information_instance = DeliveryInformation.from_json(json)
# print the JSON string representation of the object
print(DeliveryInformation.to_json())

# convert the object into a dict
delivery_information_dict = delivery_information_instance.to_dict()
# create an instance of DeliveryInformation from a dict
delivery_information_from_dict = DeliveryInformation.from_dict(delivery_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


