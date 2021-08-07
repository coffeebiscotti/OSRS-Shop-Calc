floor = int(input('What is the base price?     '))
percent_increase = float(input('What is the increase per buy' "\n" 'Ex. 1% increase = 0.01     '))
amount_per_world = int(input('How many buys per world'     ))
total_amount = int(input('How many buys total     '))

def price_calc(floor, percent_increase, amount_per_world):
	price = floor * (1+(percent_increase * (amount_per_world-1)))
	price = round(price)
	return price

def calc_world_buy(floor, percent_increase, amount_per_world):
    total = 0
    for i in range(1, amount_per_world + 1):
        total = total + price_calc(floor, percent_increase, i)
    total = round(total)
    return total

world_buys, remainder = divmod(total_amount, amount_per_world)

cost_per_world = calc_world_buy(floor, percent_increase, amount_per_world)
cost_of_remainder = calc_world_buy(floor, percent_increase, remainder)

total_cost = cost_per_world * world_buys + cost_of_remainder

print('It will cost', total_cost, 'GP to buy', total_amount)




        
