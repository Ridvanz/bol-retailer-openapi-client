# coding: utf-8

"""
    v10 - Retailer API

    The bol.com API for retailers.  # Authentication Our API requires authentication via OAuth2. The detailed steps to authenticate are explained [here](https://api.bol.com/retailer/public/Retailer-API/authentication.html)   # Demo scenarios Our API specification includes examples of the responses you can expect. For more information as well as more examples, we refer you to the following resources:   - [Demo environment](https://api.bol.com/retailer/public/Retailer-API/demo/demo.html) - [Demo scenarios](https://api.bol.com/retailer/public/Retailer-API/demo/v10-index.html) 

    The version of the OpenAPI document: 10.x
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.commissions_api import CommissionsApi


class TestCommissionsApi(unittest.TestCase):
    """CommissionsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CommissionsApi()

    def tearDown(self) -> None:
        pass

    def test_get_commission(self) -> None:
        """Test case for get_commission

        Get all commissions and reductions by EAN per single EAN
        """
        pass

    def test_get_commission_rates(self) -> None:
        """Test case for get_commission_rates

        Get a list of commissions by EAN (BETA)
        """
        pass

    def test_get_commissions(self) -> None:
        """Test case for get_commissions

        Get all commissions and reductions by EAN in bulk
        """
        pass


if __name__ == '__main__':
    unittest.main()
