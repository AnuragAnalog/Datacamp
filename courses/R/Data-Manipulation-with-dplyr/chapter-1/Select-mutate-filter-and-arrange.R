counties %>%
  # Select the five columns 
  select(state, county, population, men, women) %>%
  # Add the proportion_men variable
  mutate(proportion_men = men / population) %>%
  # Filter for population of at least 10,000
  filter(population >= 10000) %>%
  # Arrange proportion of men in descending order 
  arrange(desc(proportion_men))
