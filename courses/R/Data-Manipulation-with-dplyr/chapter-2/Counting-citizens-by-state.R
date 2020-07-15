# Find number of counties per state, weighted by citizens
counties_selected %>%
  count(state, wt = citizens, sort = TRUE)
