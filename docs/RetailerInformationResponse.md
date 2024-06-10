# RetailerInformationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retailer_id** | **str** | The Id of the retailer which information belongs to. | 
**display_name** | **str** | The name of the retailer visible on bol.com | 
**company_name** | **str** | The company name of the retailer. | 
**vat_number** | **str** | The VAT number of the retailer. | 
**kvk_number** | **str** | The KVK number of the retailer. | 
**registration_date** | **str** | A date representing the registration date for the retailer within bol.com | 
**top_retailer** | **bool** | Indication of retailer&#39;s being the top seller. | [optional] 
**rating_method** | **str** | An identifier that identifies if the rating is calculated over the past three months or on all reviews for the retailer. | [optional] 
**retailer_rating** | [**RetailerRating**](RetailerRating.md) |  | [optional] 
**retailer_review** | [**RetailerReview**](RetailerReview.md) |  | [optional] 

## Example

```python
from openapi_client.models.retailer_information_response import RetailerInformationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RetailerInformationResponse from a JSON string
retailer_information_response_instance = RetailerInformationResponse.from_json(json)
# print the JSON string representation of the object
print(RetailerInformationResponse.to_json())

# convert the object into a dict
retailer_information_response_dict = retailer_information_response_instance.to_dict()
# create an instance of RetailerInformationResponse from a dict
retailer_information_response_from_dict = RetailerInformationResponse.from_dict(retailer_information_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


