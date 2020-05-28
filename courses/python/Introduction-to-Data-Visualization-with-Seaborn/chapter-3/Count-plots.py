# Instruction1
# Create count plot of internet usage
sns.catplot(x='Internet usage', data=survey_data, kind='count')

# Show plot
plt.show()

# Instruction2
# Change the orientation of the plot
sns.catplot(y="Internet usage", data=survey_data,
            kind="count")

# Show plot
plt.show()

# Instruction3
# Create column subplots based on age category
sns.catplot(y="Internet usage", data=survey_data,
            kind="count",
            col='Age Category')

# Show plot
plt.show()
