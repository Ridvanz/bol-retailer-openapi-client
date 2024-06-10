# Campaign


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the campaign under which the promotion had been created. | 
**start_date_time** | **datetime** | The starting date and time of the campaign. | 
**end_date_time** | **datetime** | The ending date and time of the campaign. | [optional] 

## Example

```python
from openapi_client.models.campaign import Campaign

# TODO update the JSON string below
json = "{}"
# create an instance of Campaign from a JSON string
campaign_instance = Campaign.from_json(json)
# print the JSON string representation of the object
print(Campaign.to_json())

# convert the object into a dict
campaign_dict = campaign_instance.to_dict()
# create an instance of Campaign from a dict
campaign_from_dict = Campaign.from_dict(campaign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


