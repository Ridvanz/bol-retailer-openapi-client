# SearchTermsPeriod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**day** | **str** | Day number in the ISO-8601 standard. | [optional] 
**week** | **str** | Week number in the ISO-8601 standard. | [optional] 
**month** | **str** | Month number in the ISO-8601 standard. | [optional] 
**year** | **str** | Year number in the ISO-8601 standard. | [optional] 

## Example

```python
from openapi_client.models.search_terms_period import SearchTermsPeriod

# TODO update the JSON string below
json = "{}"
# create an instance of SearchTermsPeriod from a JSON string
search_terms_period_instance = SearchTermsPeriod.from_json(json)
# print the JSON string representation of the object
print(SearchTermsPeriod.to_json())

# convert the object into a dict
search_terms_period_dict = search_terms_period_instance.to_dict()
# create an instance of SearchTermsPeriod from a dict
search_terms_period_from_dict = SearchTermsPeriod.from_dict(search_terms_period_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


