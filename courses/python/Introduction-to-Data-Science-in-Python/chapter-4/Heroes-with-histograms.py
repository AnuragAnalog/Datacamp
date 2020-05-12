# Instruction1
# Create a histogram of gravel.radius
plt.hist(gravel.radius)

# Display histogram
plt.show()

# Instruction2
# Create a histogram
# Range is 2 to 8, with 40 bins
plt.hist(gravel.radius, bins=40, range=(2, 8))

# Display histogram
plt.show()

# Instruction3
# Create a histogram
# Normalize to 1
plt.hist(gravel.radius,
         bins=40,
         range=(2, 8),
         density=1)

# Display histogram
plt.show()

# Instruction4
# Create a histogram
plt.hist(gravel.radius,
         bins=40,
         range=(2, 8),
         density=True)

# Label plot
plt.xlabel('Gravel Radius (mm)')
plt.ylabel('Frequency')
plt.title('Sample from Shoeprint')

# Display histogram
plt.show()
