# coding: utf-8

"""
    v10 - Retailer API

    The bol.com API for retailers.  # Authentication Our API requires authentication via OAuth2. The detailed steps to authenticate are explained [here](https://api.bol.com/retailer/public/Retailer-API/authentication.html)   # Demo scenarios Our API specification includes examples of the responses you can expect. For more information as well as more examples, we refer you to the following resources:   - [Demo environment](https://api.bol.com/retailer/public/Retailer-API/demo/demo.html) - [Demo scenarios](https://api.bol.com/retailer/public/Retailer-API/demo/v10-index.html) 

    The version of the OpenAPI document: 10.x
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.transports_api import TransportsApi


class TestTransportsApi(unittest.TestCase):
    """TransportsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TransportsApi()

    def tearDown(self) -> None:
        pass

    def test_add_transport_information_by_transport_id(self) -> None:
        """Test case for add_transport_information_by_transport_id

        Add transport information by transport id
        """
        pass


if __name__ == '__main__':
    unittest.main()
