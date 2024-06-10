# CompetingOffersResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offers** | [**List[Offer]**](Offer.md) | List of offers. | 

## Example

```python
from openapi_client.models.competing_offers_response import CompetingOffersResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CompetingOffersResponse from a JSON string
competing_offers_response_instance = CompetingOffersResponse.from_json(json)
# print the JSON string representation of the object
print(CompetingOffersResponse.to_json())

# convert the object into a dict
competing_offers_response_dict = competing_offers_response_instance.to_dict()
# create an instance of CompetingOffersResponse from a dict
competing_offers_response_from_dict = CompetingOffersResponse.from_dict(competing_offers_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


