# Import pandas
import pandas as pd

# Create a DataFrame: df
df = pd.DataFrame(index=artist_names, data=norm_features)

# Select row of 'Bruce Springsteen': artist
artist = df.loc['Bruce Springsteen']

# Compute cosine similarities: similarities
similarities = df.dot(artist)

# Display those with highest cosine similarity
print(similarities.nlargest())

