# Instruction1
# Create bar plot of average final grade in each study category
sns.catplot(x='study_time', y='G3', data=student_data, kind='bar')

# Show plot
plt.show()

# Instruction2
# Rearrange the categories
sns.catplot(x="study_time", y="G3", data=student_data, kind="bar", order=['<2 hours', '2 to 5 hours', '5 to 10 hours', '>10 hours'])

# Show plot
plt.show()

# Instruction3
# Turn off the confidence intervals
sns.catplot(x="study_time", y="G3", data=student_data, kind="bar", order=["<2 hours", "2 to 5 hours", "5 to 10 hours", ">10 hours"], ci=None)

# Show plot
plt.show()
