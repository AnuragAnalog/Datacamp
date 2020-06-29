# View the head of census_long3
head(census_long3)

# Separate the yr_month column into two
census_long4 <- separate(census_long3, yr_month, c('year', 'month'))

# View the first 6 rows of the result
head(census_long4)
