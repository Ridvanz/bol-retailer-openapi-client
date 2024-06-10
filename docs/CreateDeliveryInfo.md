# CreateDeliveryInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected_delivery_date** | **str** | The expected delivery date of the shipment at the bol.com warehouse. In ISO 8601 format. | 
**transporter_code** | **str** | The transporter code that correlates to the transport used for this replenishment. | 

## Example

```python
from openapi_client.models.create_delivery_info import CreateDeliveryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDeliveryInfo from a JSON string
create_delivery_info_instance = CreateDeliveryInfo.from_json(json)
# print the JSON string representation of the object
print(CreateDeliveryInfo.to_json())

# convert the object into a dict
create_delivery_info_dict = create_delivery_info_instance.to_dict()
# create an instance of CreateDeliveryInfo from a dict
create_delivery_info_from_dict = CreateDeliveryInfo.from_dict(create_delivery_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


