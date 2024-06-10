# DeliveryDatesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_dates** | **List[str]** | Allowed delivery dates for shipments to the bol.com warehouse in ISO 8601 format. | 

## Example

```python
from openapi_client.models.delivery_dates_response import DeliveryDatesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DeliveryDatesResponse from a JSON string
delivery_dates_response_instance = DeliveryDatesResponse.from_json(json)
# print the JSON string representation of the object
print(DeliveryDatesResponse.to_json())

# convert the object into a dict
delivery_dates_response_dict = delivery_dates_response_instance.to_dict()
# create an instance of DeliveryDatesResponse from a dict
delivery_dates_response_from_dict = DeliveryDatesResponse.from_dict(delivery_dates_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


