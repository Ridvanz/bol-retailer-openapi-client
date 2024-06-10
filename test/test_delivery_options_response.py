# coding: utf-8

"""
    v10 - Retailer API

    The bol.com API for retailers.  # Authentication Our API requires authentication via OAuth2. The detailed steps to authenticate are explained [here](https://api.bol.com/retailer/public/Retailer-API/authentication.html)   # Demo scenarios Our API specification includes examples of the responses you can expect. For more information as well as more examples, we refer you to the following resources:   - [Demo environment](https://api.bol.com/retailer/public/Retailer-API/demo/demo.html) - [Demo scenarios](https://api.bol.com/retailer/public/Retailer-API/demo/v10-index.html) 

    The version of the OpenAPI document: 10.x
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.delivery_options_response import DeliveryOptionsResponse

class TestDeliveryOptionsResponse(unittest.TestCase):
    """DeliveryOptionsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DeliveryOptionsResponse:
        """Test DeliveryOptionsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DeliveryOptionsResponse`
        """
        model = DeliveryOptionsResponse()
        if include_optional:
            return DeliveryOptionsResponse(
                delivery_options = [
                    openapi_client.models.delivery_option.DeliveryOption(
                        shipping_label_offer_id = '027b79fa-5743-40f0-94c7-0eac761af611', 
                        recommended = True, 
                        valid_until_date = 'Sun Jan 12 00:00:00 UTC 2020', 
                        transporter_code = 'TNT', 
                        label_type = 'PARCEL', 
                        label_display_name = 'PostNL & bol.com - Pakket', 
                        label_price = openapi_client.models.label_price.LabelPrice(
                            total_price = 2.88, ), 
                        package_restrictions = openapi_client.models.package_restrictions.PackageRestrictions(
                            max_weight = '10 kg', 
                            max_dimensions = '10 x 10 x 10 cm', ), 
                        handover_details = openapi_client.models.handover_details.HandoverDetails(
                            meets_customer_expectation = True, 
                            earliest_handover_date_time = '2018-04-19T00:00+02:00', 
                            latest_handover_date_time = '2018-04-19T19:00+02:00', 
                            collection_method = 'DROP_OFF', ), )
                    ]
            )
        else:
            return DeliveryOptionsResponse(
                delivery_options = [
                    openapi_client.models.delivery_option.DeliveryOption(
                        shipping_label_offer_id = '027b79fa-5743-40f0-94c7-0eac761af611', 
                        recommended = True, 
                        valid_until_date = 'Sun Jan 12 00:00:00 UTC 2020', 
                        transporter_code = 'TNT', 
                        label_type = 'PARCEL', 
                        label_display_name = 'PostNL & bol.com - Pakket', 
                        label_price = openapi_client.models.label_price.LabelPrice(
                            total_price = 2.88, ), 
                        package_restrictions = openapi_client.models.package_restrictions.PackageRestrictions(
                            max_weight = '10 kg', 
                            max_dimensions = '10 x 10 x 10 cm', ), 
                        handover_details = openapi_client.models.handover_details.HandoverDetails(
                            meets_customer_expectation = True, 
                            earliest_handover_date_time = '2018-04-19T00:00+02:00', 
                            latest_handover_date_time = '2018-04-19T19:00+02:00', 
                            collection_method = 'DROP_OFF', ), )
                    ],
        )
        """

    def testDeliveryOptionsResponse(self):
        """Test DeliveryOptionsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()