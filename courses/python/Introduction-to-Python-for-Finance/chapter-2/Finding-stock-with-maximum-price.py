# Do not modify this
max_price = max(prices)

# Identify index of max price
max_index = prices.index(max(prices))

# Identify the name of the company with max price
max_stock_name = names[max_index]

# Fill in the blanks 
print('The largest stock price is associated with ' + max_stock_name + ' and is $' + str(max_price) + '.')
