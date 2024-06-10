# ReturnItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rma_id** | **str** | The RMA (Return Merchandise Authorization) identifier of the return. | 
**order_id** | **str** | The id of the customer order this return item is in. | 
**ean** | **str** | The EAN number associated with this product. | 
**title** | **str** | The product title. | 
**expected_quantity** | **int** | The quantity that is expected to be returned by the customer. Note: this can be greater than 1 in case the customer ordered a quantity greater than 1 of the same product in the same customer order. | 
**return_reason** | [**ReturnReason**](ReturnReason.md) |  | 
**track_and_trace** | **str** | The track and trace code that is associated with this transport. | [optional] 
**transporter_name** | **str** | The name of the transporter. | [optional] 
**handled** | **bool** | Indicates if this return item has been handled (by the retailer). | 
**processing_results** | [**List[ReturnProcessingResult]**](ReturnProcessingResult.md) |  | 
**customer_details** | [**CustomerDetails**](CustomerDetails.md) |  | 

## Example

```python
from openapi_client.models.return_item import ReturnItem

# TODO update the JSON string below
json = "{}"
# create an instance of ReturnItem from a JSON string
return_item_instance = ReturnItem.from_json(json)
# print the JSON string representation of the object
print(ReturnItem.to_json())

# convert the object into a dict
return_item_dict = return_item_instance.to_dict()
# create an instance of ReturnItem from a dict
return_item_from_dict = ReturnItem.from_dict(return_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


