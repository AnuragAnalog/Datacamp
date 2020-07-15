# Instruction1
# Add columns name_total and name_max for each name
babynames %>%
  group_by(name) %>%
  mutate(name_total = sum(number), name_max = max(number))

# Instruction2
babynames %>%
  group_by(name) %>%
  mutate(name_total = sum(number),
         name_max = max(number)) %>%
  # Ungroup the table 
  ungroup()
  # Add the fraction_max column containing the number by the name maximum 
  mutate(fraction_max = number / name_total)
