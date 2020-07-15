counties_selected %>%
  group_by(region, state) %>%
  # Calculate average income
  summarise(average_income = mean(income)) %>%
  # Find the highest income state in each region
  top_n(1, average_income)
