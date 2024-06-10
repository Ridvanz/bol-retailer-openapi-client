# CreateReturnRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_item_id** | **str** | The id for the order item. One order can have multiple order items, but the list can only take one item. | 
**quantity_returned** | **int** | The quantity of items returned. | 
**handling_result** | **str** | The handling result requested by the retailer. | 

## Example

```python
from openapi_client.models.create_return_request import CreateReturnRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateReturnRequest from a JSON string
create_return_request_instance = CreateReturnRequest.from_json(json)
# print the JSON string representation of the object
print(CreateReturnRequest.to_json())

# convert the object into a dict
create_return_request_dict = create_return_request_instance.to_dict()
# create an instance of CreateReturnRequest from a dict
create_return_request_from_dict = CreateReturnRequest.from_dict(create_return_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


