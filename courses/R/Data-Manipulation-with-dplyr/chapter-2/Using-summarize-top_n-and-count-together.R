# Instruction1
# Find the total population for each combination of state and metro
counties_selected %>%
  group_by(state, metro) %>%
  summarise(total_pop = sum(population))

# Instruction2
# Extract the most populated row for each state
counties_selected %>%
  group_by(state, metro) %>%
  summarize(total_pop = sum(population)) %>%
  top_n(1, total_pop)

# Instruction3
# Count the states with more people in Metro or Nonmetro areas
counties_selected %>%
  group_by(state, metro) %>%
  summarize(total_pop = sum(population)) %>%
  top_n(1, total_pop) %>%
  ungroup() %>%
  count(metro)
