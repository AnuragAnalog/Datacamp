# Load dplyr package
library(dplyr)

# Print the votes_processed dataset
print(votes_processed)

# Print the descriptions dataset
print(descriptions)

# Join them together based on the "rcid" and "session" columns
votes_joined <- votes_processed %>%
  inner_join(descriptions, on = c("rcid", "session"))
