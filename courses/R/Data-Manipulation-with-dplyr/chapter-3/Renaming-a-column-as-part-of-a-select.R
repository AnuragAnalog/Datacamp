# Select state, county, and poverty as poverty_rate
counties %>%
  select(state, county, poverty_rate = poverty)
