# coding: utf-8

"""
    v10 - Retailer API

    The bol.com API for retailers.  # Authentication Our API requires authentication via OAuth2. The detailed steps to authenticate are explained [here](https://api.bol.com/retailer/public/Retailer-API/authentication.html)   # Demo scenarios Our API specification includes examples of the responses you can expect. For more information as well as more examples, we refer you to the following resources:   - [Demo environment](https://api.bol.com/retailer/public/Retailer-API/demo/demo.html) - [Demo scenarios](https://api.bol.com/retailer/public/Retailer-API/demo/v10-index.html) 

    The version of the OpenAPI document: 10.x
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.product_ranks import ProductRanks

class TestProductRanks(unittest.TestCase):
    """ProductRanks unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProductRanks:
        """Test ProductRanks
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProductRanks`
        """
        model = ProductRanks()
        if include_optional:
            return ProductRanks(
                ranks = [
                    openapi_client.models.rank.Rank(
                        category_id = '53495', 
                        search_term = 'dvd', 
                        was_sponsored = False, 
                        rank = 1, 
                        impressions = 100, )
                    ],
                has_next_page = False
            )
        else:
            return ProductRanks(
                ranks = [
                    openapi_client.models.rank.Rank(
                        category_id = '53495', 
                        search_term = 'dvd', 
                        was_sponsored = False, 
                        rank = 1, 
                        impressions = 100, )
                    ],
                has_next_page = False,
        )
        """

    def testProductRanks(self):
        """Test ProductRanks"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()