# ProductRatingsRating


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rating** | **int** | Scale of the rating provided by the customer. | 
**count** | **int** | The number of ratings for the corresponding scale. | [optional] 

## Example

```python
from openapi_client.models.product_ratings_rating import ProductRatingsRating

# TODO update the JSON string below
json = "{}"
# create an instance of ProductRatingsRating from a JSON string
product_ratings_rating_instance = ProductRatingsRating.from_json(json)
# print the JSON string representation of the object
print(ProductRatingsRating.to_json())

# convert the object into a dict
product_ratings_rating_dict = product_ratings_rating_instance.to_dict()
# create an instance of ProductRatingsRating from a dict
product_ratings_rating_from_dict = ProductRatingsRating.from_dict(product_ratings_rating_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


