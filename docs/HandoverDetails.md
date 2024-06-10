# HandoverDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meets_customer_expectation** | **bool** | Indicates if you can use this label without receiving a strike if you handover before the latestHandoverDateTime. If this field is &#39;false&#39; you can still buy and use this label but it will have negative consequences on your performance score because the order will be delivered too early or too late. | [optional] 
**earliest_handover_date_time** | **datetime** | The date and time at which the parcel can be earliest  at the transporter to make sure your parcel is delivered on time. | [optional] 
**latest_handover_date_time** | **datetime** | The date and time at which the parcel must ultimately be at the transporter to make sure your parcel is delivered on time. If you handover after this date you will receive a strike because you order will be delivered too late. | [optional] 
**collection_method** | **str** | The type of collection for this parcel. | [optional] 

## Example

```python
from openapi_client.models.handover_details import HandoverDetails

# TODO update the JSON string below
json = "{}"
# create an instance of HandoverDetails from a JSON string
handover_details_instance = HandoverDetails.from_json(json)
# print the JSON string representation of the object
print(HandoverDetails.to_json())

# convert the object into a dict
handover_details_dict = handover_details_instance.to_dict()
# create an instance of HandoverDetails from a dict
handover_details_from_dict = HandoverDetails.from_dict(handover_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


