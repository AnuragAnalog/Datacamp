# Instruction1
# Create a point plot with subgroups
sns.catplot(x='romantic', y='absences', data=student_data, kind='point', hue='school')

# Show plot
plt.show()

# Instruction2
# Turn off the confidence intervals for this plot
sns.catplot(x="romantic", y="absences", data=student_data, kind="point", hue="school", ci=None)

# Show plot
plt.show()

# Instruction3
# Import median function from numpy
from numpy import median

# Plot the median number of absences instead of the mean
sns.catplot(x="romantic", y="absences", data=student_data, kind="point", hue="school", ci=None, estimator=median)

# Show plot
plt.show()
