from order_fulfillment.inventory_service import InventoryService
from order_fulfillment.notification_service import NotificationService
from order_fulfillment.order import Order
from order_fulfillment.order_client import OrderClient
from order_fulfillment.order_fulfillment_facade import OrderFulfillmentFacade
from order_fulfillment.payment_service import PaymentService
from order_fulfillment.shipping_service import ShippingService


def test_client_places_order_through_facade():
    facade = OrderFulfillmentFacade(InventoryService(), PaymentService(), ShippingService(), NotificationService())
    client = OrderClient(facade)

    steps = client.place_order(Order("O-2", "SKU-4", 59.9, "Zapopan"))

    assert steps == [
        "inventory:reserved:SKU-4",
        "payment:charged:59.90",
        "shipping:created:Zapopan",
        "notification:sent:O-2",
    ]
