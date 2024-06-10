# UpdateDeliveryInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expected_delivery_date** | **str** | The expected delivery date of the shipment at the bol.com warehouse. In ISO 8601 format. | 

## Example

```python
from openapi_client.models.update_delivery_info import UpdateDeliveryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDeliveryInfo from a JSON string
update_delivery_info_instance = UpdateDeliveryInfo.from_json(json)
# print the JSON string representation of the object
print(UpdateDeliveryInfo.to_json())

# convert the object into a dict
update_delivery_info_dict = update_delivery_info_instance.to_dict()
# create an instance of UpdateDeliveryInfo from a dict
update_delivery_info_from_dict = UpdateDeliveryInfo.from_dict(update_delivery_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


