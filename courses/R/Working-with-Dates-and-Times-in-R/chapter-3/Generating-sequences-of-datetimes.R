# Add a period of 8 hours to today
today_8am <- today() + 8 * hours()

# Sequence of two weeks from 1 to 26
every_two_weeks <- 1:26 * days()

# Create datetime for every two weeks for a year
every_two_weeks + today_8am
