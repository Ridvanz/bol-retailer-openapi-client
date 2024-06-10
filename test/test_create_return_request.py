# coding: utf-8

"""
    v10 - Retailer API

    The bol.com API for retailers.  # Authentication Our API requires authentication via OAuth2. The detailed steps to authenticate are explained [here](https://api.bol.com/retailer/public/Retailer-API/authentication.html)   # Demo scenarios Our API specification includes examples of the responses you can expect. For more information as well as more examples, we refer you to the following resources:   - [Demo environment](https://api.bol.com/retailer/public/Retailer-API/demo/demo.html) - [Demo scenarios](https://api.bol.com/retailer/public/Retailer-API/demo/v10-index.html) 

    The version of the OpenAPI document: 10.x
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.create_return_request import CreateReturnRequest

class TestCreateReturnRequest(unittest.TestCase):
    """CreateReturnRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateReturnRequest:
        """Test CreateReturnRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateReturnRequest`
        """
        model = CreateReturnRequest()
        if include_optional:
            return CreateReturnRequest(
                order_item_id = '2012345678',
                quantity_returned = 1,
                handling_result = 'RETURN_RECEIVED'
            )
        else:
            return CreateReturnRequest(
                order_item_id = '2012345678',
                quantity_returned = 1,
                handling_result = 'RETURN_RECEIVED',
        )
        """

    def testCreateReturnRequest(self):
        """Test CreateReturnRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
