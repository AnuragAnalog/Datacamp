# Head of dates
head(dates)

# Parse dates with fast_strptime
fast_strptime(dates, 
    format = '%Y-%m-%dT%H:%M:%SZ') %>% str()

# Comparse speed to ymd_hms() and fasttime
microbenchmark(
  ymd_hms = ymd_hms(dates),
  fasttime = fastPOSIXct(dates),
  fast_strptime = fast_strptime(dates, 
    format = '%Y-%m-%dT%H:%M:%SZ'),
  times = 20)
