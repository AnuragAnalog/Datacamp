# Group by region and find the greatest number of citizens who walk to work
counties_selected %>%
  group_by(region) %>%
  top_n(1, walk)
