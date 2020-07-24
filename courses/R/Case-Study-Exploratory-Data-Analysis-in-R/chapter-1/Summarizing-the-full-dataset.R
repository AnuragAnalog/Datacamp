# Print votes_processed
print(votes_processed)

# Find total and fraction of "yes" votes
votes_processed %>%
  summarise(total = n(), percent_yes = mean(vote == 1))
