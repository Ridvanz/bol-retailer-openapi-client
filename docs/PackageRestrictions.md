# PackageRestrictions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_weight** | **str** | The weight of a package. | 
**max_dimensions** | **str** | The dimensions of a package. | 

## Example

```python
from openapi_client.models.package_restrictions import PackageRestrictions

# TODO update the JSON string below
json = "{}"
# create an instance of PackageRestrictions from a JSON string
package_restrictions_instance = PackageRestrictions.from_json(json)
# print the JSON string representation of the object
print(PackageRestrictions.to_json())

# convert the object into a dict
package_restrictions_dict = package_restrictions_instance.to_dict()
# create an instance of PackageRestrictions from a dict
package_restrictions_from_dict = PackageRestrictions.from_dict(package_restrictions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


