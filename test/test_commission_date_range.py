# coding: utf-8

"""
    v10 - Retailer API

    The bol.com API for retailers.  # Authentication Our API requires authentication via OAuth2. The detailed steps to authenticate are explained [here](https://api.bol.com/retailer/public/Retailer-API/authentication.html)   # Demo scenarios Our API specification includes examples of the responses you can expect. For more information as well as more examples, we refer you to the following resources:   - [Demo environment](https://api.bol.com/retailer/public/Retailer-API/demo/demo.html) - [Demo scenarios](https://api.bol.com/retailer/public/Retailer-API/demo/v10-index.html) 

    The version of the OpenAPI document: 10.x
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.commission_date_range import CommissionDateRange

class TestCommissionDateRange(unittest.TestCase):
    """CommissionDateRange unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CommissionDateRange:
        """Test CommissionDateRange
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CommissionDateRange`
        """
        model = CommissionDateRange()
        if include_optional:
            return CommissionDateRange(
                start_date = '1970-01-01',
                end_date = '1970-01-01',
                rates = [
                    openapi_client.models.commission_date_rate.CommissionDateRate(
                        condition = 'NEW', 
                        price_ranges = [
                            openapi_client.models.commission_price_range.CommissionPriceRange(
                                range = openapi_client.models.commission_range.CommissionRange(
                                    lower = 0, 
                                    upper = 10, ), 
                                fixed_amount = 0, 
                                percentage = 20, 
                                reduction_applied = True, )
                            ], )
                    ]
            )
        else:
            return CommissionDateRange(
                start_date = '1970-01-01',
                end_date = '1970-01-01',
                rates = [
                    openapi_client.models.commission_date_rate.CommissionDateRate(
                        condition = 'NEW', 
                        price_ranges = [
                            openapi_client.models.commission_price_range.CommissionPriceRange(
                                range = openapi_client.models.commission_range.CommissionRange(
                                    lower = 0, 
                                    upper = 10, ), 
                                fixed_amount = 0, 
                                percentage = 20, 
                                reduction_applied = True, )
                            ], )
                    ],
        )
        """

    def testCommissionDateRange(self):
        """Test CommissionDateRange"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
