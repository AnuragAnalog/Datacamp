counties_selected <- counties %>%
  select(state, county, population, private_work, public_work, self_employed)

# Filter for Texas and more than 10000 people; sort in descending order of private_work
counties_selected %>%
  filter(state == 'Texas', population > 10000) %>%
  arrange(desc(private_work))
