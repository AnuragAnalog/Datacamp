# Import custom text_analyzer package
import text_analyzer

# Create a SocialMedia instance with datacamp_tweets
dc_tweets = text_analyzer.SocialMedia(text=datacamp_tweets)

# Print the top five most most mentioned users
print(dc_tweets._count_mentions().most_common(5))

# Plot the most used hashtags
text_analyzer.plot_counter(dc_tweets._count_hashtags())

