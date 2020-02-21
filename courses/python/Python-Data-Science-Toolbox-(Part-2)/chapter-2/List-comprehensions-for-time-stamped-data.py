# Extract the created_at column from df: tweet_time
tweet_time = df.created_at

# Extract the clock time: tweet_clock_time
tweet_clock_time = [info[11:19] for info in tweet_time]

# Print the extracted times
print(tweet_clock_time)

