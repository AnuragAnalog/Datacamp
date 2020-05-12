# Instruction1
# Change the marker color to red
plt.scatter(cellphone.x, cellphone.y,
           color='red')

# Add labels
plt.ylabel('Latitude')
plt.xlabel('Longitude')

# Display the plot
plt.show()

# Instruction2
# Change the marker shape to square
plt.scatter(cellphone.x, cellphone.y,
           color='red',
           marker='s')

# Add labels
plt.ylabel('Latitude')
plt.xlabel('Longitude')

# Display the plot
plt.show()

# Instruction3
# Change the transparency to 0.1
plt.scatter(cellphone.x, cellphone.y,
           color='red',
           marker='s',
           alpha=0.1)

# Add labels
plt.ylabel('Latitude')
plt.xlabel('Longitude')

# Display the plot
plt.show()
