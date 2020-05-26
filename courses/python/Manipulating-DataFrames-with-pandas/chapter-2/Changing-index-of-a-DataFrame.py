# Create the list of new indexes: new_idx
new_idx = [ind.upper() for ind in sales.index]

# Assign new_idx to sales.index
sales.index = new_idx

# Print the sales DataFrame
print(sales)
