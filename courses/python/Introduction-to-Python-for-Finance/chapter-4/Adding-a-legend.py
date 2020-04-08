# Plot stock_A and stock_B histograms
plt.hist(stock_A, bins=100, alpha=0.4, label='Stock A')
plt.hist(stock_B, bins=100, alpha=0.4, label='Stock B')

# Add the legend
plt.legend()

# Display the plot
plt.show()
