# Import numpy
import numpy as np

# Create the boolean array: too_close
too_close = election['margin'] < 1

# Assign np.nan to the 'winner' column where the results were too close to call
election['winner'][too_close] = np.nan

# Print the output of election.info()
print(election.info())

