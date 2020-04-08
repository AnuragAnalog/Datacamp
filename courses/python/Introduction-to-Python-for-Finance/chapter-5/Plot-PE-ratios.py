import matplotlib.pyplot as plt

# Make a scatterplot
plt.scatter(it_id, it_pe, color = 'red', label = 'IT')
plt.scatter(cs_id, cs_pe, color = 'green', label = 'CS')

# Add legend
plt.legend()

# Add labels
plt.xlabel('Company ID')
plt.ylabel('P/E Ratio')
plt.show()
