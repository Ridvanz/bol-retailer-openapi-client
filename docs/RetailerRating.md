# RetailerRating

Rating on different aspects all being one decimal precision.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**retailer_rating** | **float** | General rating of the retailer. | 
**product_information_rating** | **float** | Product rating of the retailer. | [optional] 
**delivery_time_rating** | **float** | Delivery rating of the retailer. | [optional] 
**shipping_rating** | **float** | Shipping rating of the retailer. | [optional] 
**service_rating** | **float** | Service rating of the retailer. | [optional] 

## Example

```python
from openapi_client.models.retailer_rating import RetailerRating

# TODO update the JSON string below
json = "{}"
# create an instance of RetailerRating from a JSON string
retailer_rating_instance = RetailerRating.from_json(json)
# print the JSON string representation of the object
print(RetailerRating.to_json())

# convert the object into a dict
retailer_rating_dict = retailer_rating_instance.to_dict()
# create an instance of RetailerRating from a dict
retailer_rating_from_dict = RetailerRating.from_dict(retailer_rating_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


