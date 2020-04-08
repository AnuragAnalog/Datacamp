# Instruction1
# Create boolean array 
boolean_array = (sectors == 'Information Technology')

# Subset sector-specific data
it_names = names[boolean_array] 
it_pe = pe[boolean_array]

# Display sector names
print(it_names)
print(it_pe)

# Instruction2
# Create boolean array 
boolean_array = (sectors == 'Consumer Staples')

# Subset sector-specific data
cs_names = names[boolean_array]
cs_pe = pe[boolean_array]

# Display sector names
print(cs_names)
print(cs_pe)
