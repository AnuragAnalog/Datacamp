# Set the number of dimensions to 2
dimensionality_reducer = PCA(n_components=2)

# Apply dimensionality reduction
tweets_reduced = dimensionality_reducer.fit_transform(tweets_matrix)

# Configure the clustering model
clustering_model = KMeans(n_clusters=2)

# Find clusters
tweet_clusters = clustering_model.fit_predict(tweets_reduced)

# Show the clustering results
print_cluster_tweets(tweet_clusters, tweets_raw)
