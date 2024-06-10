# SearchTermsCountry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | Countries in which this offer is currently on sale in the webshop in ISO-3166-1 format. | 
**value** | **int** | The number of customer visits on the search page. | 

## Example

```python
from openapi_client.models.search_terms_country import SearchTermsCountry

# TODO update the JSON string below
json = "{}"
# create an instance of SearchTermsCountry from a JSON string
search_terms_country_instance = SearchTermsCountry.from_json(json)
# print the JSON string representation of the object
print(SearchTermsCountry.to_json())

# convert the object into a dict
search_terms_country_dict = search_terms_country_instance.to_dict()
# create an instance of SearchTermsCountry from a dict
search_terms_country_from_dict = SearchTermsCountry.from_dict(search_terms_country_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


