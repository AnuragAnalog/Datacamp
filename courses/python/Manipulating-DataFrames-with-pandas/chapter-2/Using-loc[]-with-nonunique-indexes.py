# Set the index to the column 'state': sales
sales = sales.set_index('state')

# Print the sales DataFrame
print(sales)

# Access the data from 'NY'
print(sales.loc['NY'])
