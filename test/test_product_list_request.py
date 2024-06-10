# coding: utf-8

"""
    v10 - Retailer API

    The bol.com API for retailers.  # Authentication Our API requires authentication via OAuth2. The detailed steps to authenticate are explained [here](https://api.bol.com/retailer/public/Retailer-API/authentication.html)   # Demo scenarios Our API specification includes examples of the responses you can expect. For more information as well as more examples, we refer you to the following resources:   - [Demo environment](https://api.bol.com/retailer/public/Retailer-API/demo/demo.html) - [Demo scenarios](https://api.bol.com/retailer/public/Retailer-API/demo/v10-index.html) 

    The version of the OpenAPI document: 10.x
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.product_list_request import ProductListRequest

class TestProductListRequest(unittest.TestCase):
    """ProductListRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductListRequest:
        """Test ProductListRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductListRequest`
        """
        model = ProductListRequest()
        if include_optional:
            return ProductListRequest(
                country_code = 'NL',
                search_term = 'laptop',
                category_id = '4770',
                filter_ranges = [
                    openapi_client.models.product_list_filter_range.ProductListFilterRange(
                        range_id = 'PRICE', 
                        min = 1.337, 
                        max = 1.337, )
                    ],
                filter_values = [
                    openapi_client.models.product_list_filter_value.ProductListFilterValue(
                        filter_value_id = '30639', )
                    ],
                sort = 'RELEVANCE',
                page = 1
            )
        else:
            return ProductListRequest(
                page = 1,
        )
        """

    def testProductListRequest(self):
        """Test ProductListRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()