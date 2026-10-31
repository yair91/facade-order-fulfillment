from .order import Order
from .order_fulfillment_facade import OrderFulfillmentFacade


class OrderClient:
    def __init__(self, fulfillment: OrderFulfillmentFacade):
        self.fulfillment = fulfillment

    def place_order(self, order: Order) -> list[str]:
        return self.fulfillment.place_order(order)
