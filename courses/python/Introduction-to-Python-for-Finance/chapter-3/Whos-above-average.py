# Find the mean
price_mean = np.mean(prices)

# Create boolean array
boolean_array = prices > price_mean
print(boolean_array)

# Select prices that are greater than average
above_avg = prices[prices>price_mean]
print(above_avg)

