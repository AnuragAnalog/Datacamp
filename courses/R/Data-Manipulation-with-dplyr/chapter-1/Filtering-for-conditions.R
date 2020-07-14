# Instruction1
counties_selected <- counties %>%
  select(state, county, population)

# Filter for counties with a population above 1000000
counties_selected %>%
  filter(population > 1000000)

# Instruction2
counties_selected <- counties %>%
  select(state, county, population)

# Filter for counties in the state of California that have a population above 1000000
counties_selected %>%
  filter(population > 1000000, state == 'California')
