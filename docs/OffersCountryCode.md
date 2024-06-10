# OffersCountryCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | Countries in which this offer is currently on sale in the webshop, in ISO-3166-1 format. | 

## Example

```python
from openapi_client.models.offers_country_code import OffersCountryCode

# TODO update the JSON string below
json = "{}"
# create an instance of OffersCountryCode from a JSON string
offers_country_code_instance = OffersCountryCode.from_json(json)
# print the JSON string representation of the object
print(OffersCountryCode.to_json())

# convert the object into a dict
offers_country_code_dict = offers_country_code_instance.to_dict()
# create an instance of OffersCountryCode from a dict
offers_country_code_from_dict = OffersCountryCode.from_dict(offers_country_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


