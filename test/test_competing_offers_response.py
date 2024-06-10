# coding: utf-8

"""
    v10 - Retailer API

    The bol.com API for retailers.  # Authentication Our API requires authentication via OAuth2. The detailed steps to authenticate are explained [here](https://api.bol.com/retailer/public/Retailer-API/authentication.html)   # Demo scenarios Our API specification includes examples of the responses you can expect. For more information as well as more examples, we refer you to the following resources:   - [Demo environment](https://api.bol.com/retailer/public/Retailer-API/demo/demo.html) - [Demo scenarios](https://api.bol.com/retailer/public/Retailer-API/demo/v10-index.html) 

    The version of the OpenAPI document: 10.x
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.competing_offers_response import CompetingOffersResponse

class TestCompetingOffersResponse(unittest.TestCase):
    """CompetingOffersResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CompetingOffersResponse:
        """Test CompetingOffersResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CompetingOffersResponse`
        """
        model = CompetingOffersResponse()
        if include_optional:
            return CompetingOffersResponse(
                offers = [
                    openapi_client.models.offer.Offer(
                        offer_id = '228b6d06-2067-4cef-8447-c21d0c233e61', 
                        retailer_id = '0', 
                        country_code = 'NL', 
                        best_offer = True, 
                        price = 41.5, 
                        fulfilment_method = 'FBB', 
                        condition = 'NEW', 
                        ultimate_order_time = '23:59', 
                        min_delivery_date = 'Thu Oct 20 00:00:00 UTC 2022', 
                        max_delivery_date = 'Fri Oct 21 00:00:00 UTC 2022', )
                    ]
            )
        else:
            return CompetingOffersResponse(
                offers = [
                    openapi_client.models.offer.Offer(
                        offer_id = '228b6d06-2067-4cef-8447-c21d0c233e61', 
                        retailer_id = '0', 
                        country_code = 'NL', 
                        best_offer = True, 
                        price = 41.5, 
                        fulfilment_method = 'FBB', 
                        condition = 'NEW', 
                        ultimate_order_time = '23:59', 
                        min_delivery_date = 'Thu Oct 20 00:00:00 UTC 2022', 
                        max_delivery_date = 'Fri Oct 21 00:00:00 UTC 2022', )
                    ],
        )
        """

    def testCompetingOffersResponse(self):
        """Test CompetingOffersResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
