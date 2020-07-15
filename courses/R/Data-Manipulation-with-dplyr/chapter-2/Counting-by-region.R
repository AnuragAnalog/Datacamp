# Use count to find the number of counties in each region
counties_selected %>%
  count(region, sort = TRUE)
