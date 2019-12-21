from before_strategy.order import Order
from before_strategy.shipping_cost import ShippingCost
from before_strategy.shipper import Shipper

# Test FedEx
order = Order(Shipper.fedex)
cost_calculator = ShippingCost()
cost = cost_calculator.shipping_cost(order)
assert cost == 3.0
print("Test passed")

# Test UPS
order = Order(Shipper.ups)
cost_calculator = ShippingCost()
cost = cost_calculator.shipping_cost(order)
assert cost == 4.0
print("Test passed")

# Test Post
order = Order(Shipper.post)
cost_calculator = ShippingCost()
cost = cost_calculator.shipping_cost(order)
assert cost == 5.0
print("Test passed")
