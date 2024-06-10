# Offer

List of offers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offer_id** | **str** | Unique identifier for an offer. | 
**retailer_id** | **str** | The ID of the retailer which the offer belongs to. | 
**country_code** | **str** | The country code. | 
**best_offer** | **bool** | Indicator if the offer is the best offer within the country for the requested EAN. | 
**price** | **float** | The selling price to the customer of a single unit including VAT unless there is a discount. The price should always have two decimals precision. | 
**fulfilment_method** | **str** | The fulfilment method. Fulfilled by the retailer (FBR) or fulfilled by bol.com (FBB). | 
**condition** | **str** | The condition of the offered product. | [optional] 
**ultimate_order_time** | **str** | The time in ISO 8601 format when the ultimate order time on the day in order to comply to the maxDeliveryDate as a promise. | [optional] 
**min_delivery_date** | **date** | The date at which package can be delivered to customer earliest. | [optional] 
**max_delivery_date** | **date** | The date at which package can be delivered to customer latest. In case of pre-orders where a specific delivery date is not available, this field will not be present. | [optional] 

## Example

```python
from openapi_client.models.offer import Offer

# TODO update the JSON string below
json = "{}"
# create an instance of Offer from a JSON string
offer_instance = Offer.from_json(json)
# print the JSON string representation of the object
print(Offer.to_json())

# convert the object into a dict
offer_dict = offer_instance.to_dict()
# create an instance of Offer from a dict
offer_from_dict = Offer.from_dict(offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


