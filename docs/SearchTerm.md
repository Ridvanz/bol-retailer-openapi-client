# SearchTerm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_term** | **str** | The search term for which you requested the search volume. | 
**type** | **str** | Interpretation of the data that applies to this measurement. | 
**total** | **int** | The number of customer visits on the search page. | 
**countries** | [**List[SearchTermsCountry]**](SearchTermsCountry.md) |  | 
**periods** | [**List[TotalPeriod]**](TotalPeriod.md) |  | 
**related_search_terms** | [**List[RelatedSearchTerm]**](RelatedSearchTerm.md) |  | [optional] 

## Example

```python
from openapi_client.models.search_term import SearchTerm

# TODO update the JSON string below
json = "{}"
# create an instance of SearchTerm from a JSON string
search_term_instance = SearchTerm.from_json(json)
# print the JSON string representation of the object
print(SearchTerm.to_json())

# convert the object into a dict
search_term_dict = search_term_instance.to_dict()
# create an instance of SearchTerm from a dict
search_term_from_dict = SearchTerm.from_dict(search_term_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


