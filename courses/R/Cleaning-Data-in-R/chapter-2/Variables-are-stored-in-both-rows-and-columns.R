# View first 50 rows of census_long
head(census_long, n = 50)

# Spread the type column
census_long2 <- spread(census_long, type, amount)

# View first 20 rows of census_long2
head(census_long2, n = 20)
