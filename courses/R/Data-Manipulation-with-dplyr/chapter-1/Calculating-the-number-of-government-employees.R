# Instruction1
counties_selected <- counties %>%
  select(state, county, population, public_work)

# Add a new column public_workers with the number of people employed in public work
counties_selected %>%
  mutate(public_workers = public_work * population / 100)

# Instruction2
counties_selected <- counties %>%
  select(state, county, population, public_work)

# Sort in descending order of the public_workers column
counties_selected %>%
  mutate(public_workers = public_work * population / 100) %>%
  arrange(desc(public_workers))
