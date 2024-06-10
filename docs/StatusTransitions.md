# StatusTransitions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Indicates the status of this invoice request. | 
**status_date_time** | **datetime** | The date and time in ISO 8601 format that indicates when this status was updated for this invoice request. | 

## Example

```python
from openapi_client.models.status_transitions import StatusTransitions

# TODO update the JSON string below
json = "{}"
# create an instance of StatusTransitions from a JSON string
status_transitions_instance = StatusTransitions.from_json(json)
# print the JSON string representation of the object
print(StatusTransitions.to_json())

# convert the object into a dict
status_transitions_dict = status_transitions_instance.to_dict()
# create an instance of StatusTransitions from a dict
status_transitions_from_dict = StatusTransitions.from_dict(status_transitions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


