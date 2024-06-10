# RelatedSearchTerm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | The number of customer visits on the search page. | 
**search_term** | **str** | The search term for which you requested the search volume. | 

## Example

```python
from openapi_client.models.related_search_term import RelatedSearchTerm

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedSearchTerm from a JSON string
related_search_term_instance = RelatedSearchTerm.from_json(json)
# print the JSON string representation of the object
print(RelatedSearchTerm.to_json())

# convert the object into a dict
related_search_term_dict = related_search_term_instance.to_dict()
# create an instance of RelatedSearchTerm from a dict
related_search_term_from_dict = RelatedSearchTerm.from_dict(related_search_term_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


