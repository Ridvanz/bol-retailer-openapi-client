# coding: utf-8

"""
    v10 - Retailer API

    The bol.com API for retailers.  # Authentication Our API requires authentication via OAuth2. The detailed steps to authenticate are explained [here](https://api.bol.com/retailer/public/Retailer-API/authentication.html)   # Demo scenarios Our API specification includes examples of the responses you can expect. For more information as well as more examples, we refer you to the following resources:   - [Demo environment](https://api.bol.com/retailer/public/Retailer-API/demo/demo.html) - [Demo scenarios](https://api.bol.com/retailer/public/Retailer-API/demo/v10-index.html) 

    The version of the OpenAPI document: 10.x
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.process_status import ProcessStatus

class TestProcessStatus(unittest.TestCase):
    """ProcessStatus unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProcessStatus:
        """Test ProcessStatus
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProcessStatus`
        """
        model = ProcessStatus()
        if include_optional:
            return ProcessStatus(
                process_status_id = '1234567',
                entity_id = '987654321',
                event_type = 'CONFIRM_SHIPMENT',
                description = 'Example process status description for processing 987654321.',
                status = 'SUCCESS',
                error_message = 'Example process status error message.',
                create_timestamp = '2018-11-14T09:34:41+01:00',
                links = [
                    openapi_client.models.link.Link(
                        rel = '', 
                        href = '', 
                        hreflang = '', 
                        media = '', 
                        title = '', 
                        type = '', 
                        deprecation = '', 
                        profile = '', 
                        name = '', )
                    ]
            )
        else:
            return ProcessStatus(
                event_type = 'CONFIRM_SHIPMENT',
                description = 'Example process status description for processing 987654321.',
                status = 'SUCCESS',
                create_timestamp = '2018-11-14T09:34:41+01:00',
                links = [
                    openapi_client.models.link.Link(
                        rel = '', 
                        href = '', 
                        hreflang = '', 
                        media = '', 
                        title = '', 
                        type = '', 
                        deprecation = '', 
                        profile = '', 
                        name = '', )
                    ],
        )
        """

    def testProcessStatus(self):
        """Test ProcessStatus"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
