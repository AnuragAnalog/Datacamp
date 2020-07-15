# Instruction1
# Summarize to find the total population
counties_selected %>%
  group_by(region, state) %>%
  summarise(total_pop = sum(population))

# Instruction2
# Calculate the average_pop and median_pop columns 
counties_selected %>%
  group_by(region, state) %>%
  summarize(total_pop = sum(population)) %>%
  summarize(average_pop = mean(total_pop), median_pop = median(total_pop))

