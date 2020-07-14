# New columns for duration and period
monarchs <- monarchs %>%
  mutate(
    duration = as.duration(reign),
    period = as.period(reign))
    
# Examine results    
monarchs %>%
  select(name, duration, period)
