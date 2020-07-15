# Find the most common name in each year
babynames %>%
  group_by(year) %>%
  top_n(1, number)
