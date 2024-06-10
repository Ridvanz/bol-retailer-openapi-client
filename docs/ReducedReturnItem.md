# ReducedReturnItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rma_id** | **str** | The RMA (Return Merchandise Authorization) identifier of the return. | 
**order_id** | **str** | The id of the customer order this return item is in. | 
**ean** | **str** | The EAN number associated with this product. | 
**expected_quantity** | **int** | The quantity that is expected to be returned by the customer. Note: this can be greater than 1 in case the customer ordered a quantity greater than 1 of the same product in the same customer order. | 
**return_reason** | [**ReturnReason**](ReturnReason.md) |  | 
**handled** | **bool** | Indicates if this return item has been handled (by the retailer). | 
**processing_results** | [**List[ReturnProcessingResult]**](ReturnProcessingResult.md) |  | 

## Example

```python
from openapi_client.models.reduced_return_item import ReducedReturnItem

# TODO update the JSON string below
json = "{}"
# create an instance of ReducedReturnItem from a JSON string
reduced_return_item_instance = ReducedReturnItem.from_json(json)
# print the JSON string representation of the object
print(ReducedReturnItem.to_json())

# convert the object into a dict
reduced_return_item_dict = reduced_return_item_instance.to_dict()
# create an instance of ReducedReturnItem from a dict
reduced_return_item_from_dict = ReducedReturnItem.from_dict(reduced_return_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


