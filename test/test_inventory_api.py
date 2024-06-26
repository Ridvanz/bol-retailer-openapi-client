# coding: utf-8

"""
    v10 - Retailer API

    The bol.com API for retailers.  # Authentication Our API requires authentication via OAuth2. The detailed steps to authenticate are explained [here](https://api.bol.com/retailer/public/Retailer-API/authentication.html)   # Demo scenarios Our API specification includes examples of the responses you can expect. For more information as well as more examples, we refer you to the following resources:   - [Demo environment](https://api.bol.com/retailer/public/Retailer-API/demo/demo.html) - [Demo scenarios](https://api.bol.com/retailer/public/Retailer-API/demo/v10-index.html) 

    The version of the OpenAPI document: 10.x
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.inventory_api import InventoryApi


class TestInventoryApi(unittest.TestCase):
    """InventoryApi unit test stubs"""

    def setUp(self) -> None:
        self.api = InventoryApi()

    def tearDown(self) -> None:
        pass

    def test_get_inventory(self) -> None:
        """Test case for get_inventory

        Get LVB/FBB inventory
        """
        pass


if __name__ == '__main__':
    unittest.main()
