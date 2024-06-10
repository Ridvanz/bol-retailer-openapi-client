# StateTransition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **str** | Indicates the state of this replenishment order. | 
**state_date_time** | **datetime** | The date and time in ISO 8601 format that indicates when this states was updated for this replenishment. | 

## Example

```python
from openapi_client.models.state_transition import StateTransition

# TODO update the JSON string below
json = "{}"
# create an instance of StateTransition from a JSON string
state_transition_instance = StateTransition.from_json(json)
# print the JSON string representation of the object
print(StateTransition.to_json())

# convert the object into a dict
state_transition_dict = state_transition_instance.to_dict()
# create an instance of StateTransition from a dict
state_transition_from_dict = StateTransition.from_dict(state_transition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


