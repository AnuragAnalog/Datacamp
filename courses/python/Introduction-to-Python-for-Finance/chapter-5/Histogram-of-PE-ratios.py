# Import matplotlib.pyplot with the alias plt
import matplotlib.pyplot as plt

# Plot histogram 
plt.hist(it_pe, bins = 8)

# Add x-label
plt.xlabel('P/E ratio')

# Add y-label
plt.ylabel('Frequency')

# Show plot
plt.show()

