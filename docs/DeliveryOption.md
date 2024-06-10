# DeliveryOption

A delivery option shows how and the costs of a transport for a shippable configuration

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipping_label_offer_id** | **str** | Unique identifier for the shipping label offer. | 
**recommended** | **bool** | Indicates whether this delivery option is recommended to be the best option to ship your order item(s) with. | 
**valid_until_date** | **date** | The date until the delivery option (incl total price) is valid. | [optional] 
**transporter_code** | **str** | A code representing the transporter which is being used for transportation. | 
**label_type** | **str** | The type of the label, representing the way an item is being transported. MAILBOX is a mailbox package with delivery scan. MAILBOX_LIGHT is a mailbox package without delivery scan. PARCEL is a normal package. | 
**label_display_name** | **str** | The display name of the shipping label. | 
**label_price** | [**LabelPrice**](LabelPrice.md) |  | 
**package_restrictions** | [**PackageRestrictions**](PackageRestrictions.md) |  | 
**handover_details** | [**HandoverDetails**](HandoverDetails.md) |  | [optional] 

## Example

```python
from openapi_client.models.delivery_option import DeliveryOption

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryOption from a JSON string
delivery_option_instance = DeliveryOption.from_json(json)
# print the JSON string representation of the object
print(DeliveryOption.to_json())

# convert the object into a dict
delivery_option_dict = delivery_option_instance.to_dict()
# create an instance of DeliveryOption from a dict
delivery_option_from_dict = DeliveryOption.from_dict(delivery_option_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


