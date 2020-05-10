hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]
total_price=0
le=len(prices)
for x in  prices :
  total_price=total_price+x
average_price =total_price/le
print("Average Haircut Price:",average_price )
new_prices=[]
for x in prices:
  y=x-5
  new_prices.append(y)
# the above thig can be done in other method as well new_prices = [price - 5 for price in prices]

print(new_prices)
#Revenue
total_revenue =0
for x in range(len(hairstyles)):
  i=x
  total_revenue =prices[i]+last_week[i]
print("Total Revenue:",total_revenue)
average_daily_revenue =total_revenue /7
print(average_daily_revenue)
cuts_under_30 =[hairstyles[i] for i in
range(len(hairstyles))if new_prices[i]<30]
print(cuts_under_30)
