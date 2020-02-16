
# Create a list of strings: lannister
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Create a generator object: lengths
lengths = (len(l) for l in lannister)

# Iterate over and print the values in lengths
for value in lengths:
    print(value)

