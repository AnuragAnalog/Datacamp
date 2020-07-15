# Instruction1
# Count the number of counties in each state
counties %>%
  count(state)

# Instruction2
# Rename the n column to num_counties
counties %>%
  count(state) %>%
  rename(num_counties = n)
