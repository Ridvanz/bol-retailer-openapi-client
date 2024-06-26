# coding: utf-8

"""
    v10 - Retailer API

    The bol.com API for retailers.  # Authentication Our API requires authentication via OAuth2. The detailed steps to authenticate are explained [here](https://api.bol.com/retailer/public/Retailer-API/authentication.html)   # Demo scenarios Our API specification includes examples of the responses you can expect. For more information as well as more examples, we refer you to the following resources:   - [Demo environment](https://api.bol.com/retailer/public/Retailer-API/demo/demo.html) - [Demo scenarios](https://api.bol.com/retailer/public/Retailer-API/demo/v10-index.html) 

    The version of the OpenAPI document: 10.x
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.load_carrier import LoadCarrier

class TestLoadCarrier(unittest.TestCase):
    """LoadCarrier unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LoadCarrier:
        """Test LoadCarrier
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LoadCarrier`
        """
        model = LoadCarrier()
        if include_optional:
            return LoadCarrier(
                sscc = '020001200000007000',
                transport_label_track_and_trace = '3SJTXX216692157',
                transport_state = 'ANNOUNCED',
                transport_state_update_date_time = '2021-01-02T09:00+01:00'
            )
        else:
            return LoadCarrier(
                transport_state = 'ANNOUNCED',
                transport_state_update_date_time = '2021-01-02T09:00+01:00',
        )
        """

    def testLoadCarrier(self):
        """Test LoadCarrier"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
