# Import pandas
import pandas as pd

# Create a pandas DataFrame: df
df = pd.DataFrame(index=titles, data=nmf_features)

# Print the row for 'Anne Hathaway'
print(df.loc['Anne Hathaway'])

# Print the row for 'Denzel Washington'
print(df.loc['Denzel Washington'])

