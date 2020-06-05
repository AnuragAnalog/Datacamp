# li_df is pre-loaded in your workspace

# Select the second column, named day2, from li_df: second
second = li_df$day2

# Build a logical vector, TRUE if value in second is extreme: extremes
extremes = second < 5 | second > 25

# Count the number of TRUEs in extremes
sum(extremes)
