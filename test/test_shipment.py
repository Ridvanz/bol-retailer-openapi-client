# coding: utf-8

"""
    v10 - Retailer API

    The bol.com API for retailers.  # Authentication Our API requires authentication via OAuth2. The detailed steps to authenticate are explained [here](https://api.bol.com/retailer/public/Retailer-API/authentication.html)   # Demo scenarios Our API specification includes examples of the responses you can expect. For more information as well as more examples, we refer you to the following resources:   - [Demo environment](https://api.bol.com/retailer/public/Retailer-API/demo/demo.html) - [Demo scenarios](https://api.bol.com/retailer/public/Retailer-API/demo/v10-index.html) 

    The version of the OpenAPI document: 10.x
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.shipment import Shipment

class TestShipment(unittest.TestCase):
    """Shipment unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Shipment:
        """Test Shipment
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Shipment`
        """
        model = Shipment()
        if include_optional:
            return Shipment(
                shipment_id = '541757635',
                shipment_date_time = '2018-04-17T10:55:37+02:00',
                shipment_reference = 'BOLCOM001',
                pickup_point = True,
                order = openapi_client.models.shipment_order.ShipmentOrder(
                    order_id = '4123456789', 
                    order_placed_date_time = '2018-04-17T10:55:37+02:00', ),
                shipment_details = openapi_client.models.shipment_details.ShipmentDetails(
                    pickup_point_name = 'Albert Heijn: UTRECHT', 
                    salutation = 'MALE', 
                    first_name = 'Billie', 
                    surname = 'Jansen', 
                    street_name = 'Dorpstraat', 
                    house_number = '1', 
                    house_number_extension = 'B', 
                    extra_address_information = 'Apartment', 
                    zip_code = '1111ZZ', 
                    city = 'Utrecht', 
                    country_code = 'NL', 
                    email = 'billie@verkopen.bol.com', 
                    company = 'bol.com', 
                    delivery_phone_number = '012123456', 
                    language = 'nl', ),
                billing_details = openapi_client.models.billing_details.BillingDetails(
                    salutation = 'MALE', 
                    first_name = 'Billie', 
                    surname = 'Jansen', 
                    street_name = 'Dorpstraat', 
                    house_number = '1', 
                    house_number_extension = 'B', 
                    extra_address_information = 'Apartment', 
                    zip_code = '1111ZZ', 
                    city = 'Utrecht', 
                    country_code = 'NL', 
                    email = 'billie@verkopen.bol.com', 
                    company = 'bol.com', 
                    vat_number = 'NL999999999B99', 
                    kvk_number = '99887766', 
                    order_reference = 'MijnReferentie', ),
                shipment_items = [
                    openapi_client.models.shipment_item.ShipmentItem(
                        order_item_id = '1234567891', 
                        fulfilment = openapi_client.models.shipment_fulfilment.ShipmentFulfilment(
                            method = 'FBR', 
                            distribution_party = 'RETAILER', 
                            latest_delivery_date = 'Fri Feb 10 00:00:00 UTC 2017', ), 
                        offer = openapi_client.models.order_offer.OrderOffer(
                            offer_id = '6ff736b5-cdd0-4150-8c67-78269ee986f5', 
                            reference = 'BOLCOM00123', ), 
                        product = openapi_client.models.order_product.OrderProduct(
                            ean = '0000007740404', 
                            title = 'Product Title', ), 
                        quantity = 10, 
                        unit_price = 12.99, 
                        commission = 5.0, )
                    ],
                transport = openapi_client.models.shipment_transport.ShipmentTransport(
                    transport_id = '312778947', 
                    transporter_code = 'TNT', 
                    track_and_trace = '3SBOL0987654321', 
                    shipping_label_id = '123456789', 
                    transport_events = [
                        openapi_client.models.transport_event.TransportEvent(
                            event_code = 'AT_TRANSPORTER', 
                            event_date_time = '2021-07-28T17:21:07+02:00', )
                        ], )
            )
        else:
            return Shipment(
                shipment_id = '541757635',
                shipment_reference = 'BOLCOM001',
                order = openapi_client.models.shipment_order.ShipmentOrder(
                    order_id = '4123456789', 
                    order_placed_date_time = '2018-04-17T10:55:37+02:00', ),
                shipment_items = [
                    openapi_client.models.shipment_item.ShipmentItem(
                        order_item_id = '1234567891', 
                        fulfilment = openapi_client.models.shipment_fulfilment.ShipmentFulfilment(
                            method = 'FBR', 
                            distribution_party = 'RETAILER', 
                            latest_delivery_date = 'Fri Feb 10 00:00:00 UTC 2017', ), 
                        offer = openapi_client.models.order_offer.OrderOffer(
                            offer_id = '6ff736b5-cdd0-4150-8c67-78269ee986f5', 
                            reference = 'BOLCOM00123', ), 
                        product = openapi_client.models.order_product.OrderProduct(
                            ean = '0000007740404', 
                            title = 'Product Title', ), 
                        quantity = 10, 
                        unit_price = 12.99, 
                        commission = 5.0, )
                    ],
        )
        """

    def testShipment(self):
        """Test Shipment"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
