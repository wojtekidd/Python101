from before_strategy.shipper import Shipper


class ShippingCost:
    def shipping_cost(self, order):
        if order.shipper == Shipper.fedex:
            return self._fedex_cost(order)
        elif order.shipper == Shipper.ups:
            return self._ups_cost(order)
        elif order.shipper == Shipper.post:
            return self._post_cost(order)


    def _fedex_cost(self, order):
        return 3.0


    def _ups_cost(self, order):
        return 4.0


    def _post_cost(self, order):
        return 5.0
