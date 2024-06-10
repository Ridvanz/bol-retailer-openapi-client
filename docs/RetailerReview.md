# RetailerReview


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_review_count** | **int** | The total amount of customer review during that rating method period. | 
**approval_percentage** | **int** | The percentage of the amount of customer that rated the retailer either neutral or positive during the rating method period. | [optional] 
**positive_review_count** | **int** | The amount of positive customer reviews during that rating method period. | 
**neutral_review_count** | **int** | The amount of neutral customer reviews during that rating method period. | 
**negative_review_count** | **int** | The amount of negative customer reviews during that rating method period. | 

## Example

```python
from openapi_client.models.retailer_review import RetailerReview

# TODO update the JSON string below
json = "{}"
# create an instance of RetailerReview from a JSON string
retailer_review_instance = RetailerReview.from_json(json)
# print the JSON string representation of the object
print(RetailerReview.to_json())

# convert the object into a dict
retailer_review_dict = retailer_review_instance.to_dict()
# create an instance of RetailerReview from a dict
retailer_review_from_dict = RetailerReview.from_dict(retailer_review_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


