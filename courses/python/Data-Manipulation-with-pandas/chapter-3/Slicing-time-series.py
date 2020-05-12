# Use Boolean conditions to subset temperatures for rows in 2010 and 2011
print(temperatures[temperatures['date'] >= '2010-01-01'][temperatures['date'] <= '2011-12-31'])

# Set date as an index
temperatures_ind = temperatures.set_index('date')

# Use .loc[] to subset temperatures_ind for rows in 2010 and 2011
print(temperatures_ind.loc['2010':'2011'])

# Use .loc[] to subset temperatures_ind for rows from Aug 2010 to Feb 2011
print(temperatures_ind.loc['08-2010':'02-2011'])
