# Enrichment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** | The current enrichment level of the product. | 

## Example

```python
from openapi_client.models.enrichment import Enrichment

# TODO update the JSON string below
json = "{}"
# create an instance of Enrichment from a JSON string
enrichment_instance = Enrichment.from_json(json)
# print the JSON string representation of the object
print(Enrichment.to_json())

# convert the object into a dict
enrichment_dict = enrichment_instance.to_dict()
# create an instance of Enrichment from a dict
enrichment_from_dict = Enrichment.from_dict(enrichment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


