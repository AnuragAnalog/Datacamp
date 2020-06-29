# View the head of census
head(census)

# Gather the month columns
census2 <- gather(census, month, amount, -YEAR)

# Arrange rows by YEAR using dplyr's arrange
census2_arr <- arrange(census2, YEAR)

# View first 20 rows of census2_arr
head(census2_arr, n = 20)
