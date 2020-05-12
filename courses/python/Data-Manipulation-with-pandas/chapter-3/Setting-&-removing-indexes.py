# Look at temperatures
print(temperatures)

# Index temperatures by city
temperatures_ind = temperatures.set_index(['city'])

# Look at temperatures_ind
print(temperatures_ind)

# Reset the index, keeping its contents
print(temperatures_ind.reset_index())

# Reset the index, dropping its contents
print(temperatures_ind.reset_index(drop=True))
