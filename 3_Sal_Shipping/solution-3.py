def ground_shipping(weight):
  if weight <= 2:
    cost_per_weight = 1.5
  elif weight > 2 and weight <= 6:
    cost_per_weight = 3
  elif weight > 6 and weight <= 10:
    cost_per_weight = 4 
  elif weight > 10:
    cost_per_weight = 4.75
  cost = cost_per_weight * weight + 20
  return(cost)
  
def drone_shipping(weight):
  if weight <= 2:
    cost = weight * 4.5
    return(cost)
  if weight > 2 and weight <= 6:
    cost = weight * 9
    return(cost)
  if weight > 6 and weight <= 10:
    cost = weight * 12
    return(cost)
  if weight > 10:
    cost = weight * 14.25
    return(cost)
  
pre_ground_shipping = 125
  
def cheapest_shipping(weight):
  ground = ground_shipping(weight)
  drone = drone_shipping(weight)
  premium = pre_ground_shipping
  if ground < drone and ground < premium:
    cheapest = "ground shipping"
    cost = ground
  elif drone < ground and drone < premium:
    cheapest = "drone shipping"
    cost = drone
  elif premium < ground and premium < drone:
    cheapest = "premium ground shipping"
    cost = premium
  
  return("\nThe cheapest shipping is " + str(cheapest) + ". The cost is " + str(cost))
  
price_ground = ground_shipping(8.4)
price_drone = drone_shipping(1.5)
package_1 = cheapest_shipping(4.8)
package_2 = cheapest_shipping(41.5)

print(price_ground, price_drone, package_1, package_2)