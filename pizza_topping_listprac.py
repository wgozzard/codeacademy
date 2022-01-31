# Your code below:
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

prices = [2, 6, 1, 3, 2, 7, 2]

#Count number of $2 slices
num_two_dollar_slices = prices.count(2)

#How many toppings in the list toppings
num_pizzas = len(toppings)

#print("We sell {} different kinds of pizza!".format(num_pizzas))

#Combine two lists so that price come before toppings
pizza_and_prices = [[prices, toppings] for prices, toppings in zip(prices, toppings)]

#sort list by price low to high
pizza_and_prices.sort()

#Find cheapest
cheapest_pizza = pizza_and_prices[0]
#Find most expensive
priciest_pizza = pizza_and_prices[-1]

#Most espensive purchase, remove from list of toppings
pizza_and_prices.pop()

#Adding ingredient, keep in line with current sort
pizza_and_prices.insert(-2, [2.5, "peppers"])

#find the 3 cheapest
three_cheapest = pizza_and_prices[:3]

print(three_cheapest)
