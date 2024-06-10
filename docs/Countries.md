# Countries


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**country_code** | **str** | Countries in which this offer is currently on sale in the webshop, in ISO-3166-1 format. | [optional] 
**minimum** | **float** | Minimum number of estimated sales expectations on the bol.com platform. | 
**maximum** | **float** | Maximum number of estimated sales expectations on the bol.com platform. | 

## Example

```python
from openapi_client.models.countries import Countries

# TODO update the JSON string below
json = "{}"
# create an instance of Countries from a JSON string
countries_instance = Countries.from_json(json)
# print the JSON string representation of the object
print(Countries.to_json())

# convert the object into a dict
countries_dict = countries_instance.to_dict()
# create an instance of Countries from a dict
countries_from_dict = Countries.from_dict(countries_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


