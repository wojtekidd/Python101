from strategy.order import Order
from strategy.shipping_cost import ShippingCost
from strategy.fedex_strategy import FedexStrategy
from strategy.ups_strategy import UPSStrategy
from strategy.postal_strategy import PostalStrategy

# Test Federal Express shipping
order = Order()
strategy = FedexStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 3.0

# Test UPS shipping
order = Order()
strategy = UPSStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 4.0

# Test postal shipping
order = Order()
strategy = PostalStrategy()
cost_calculator = ShippingCost(strategy)
cost = cost_calculator.shipping_cost(order)
assert cost == 5.0
