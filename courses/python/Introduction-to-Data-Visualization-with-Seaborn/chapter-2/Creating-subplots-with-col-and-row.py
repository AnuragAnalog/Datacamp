# Instruction1
# Change to use relplot() instead of scatterplot()
sns.relplot(x="absences", y="G3", data=student_data, kind='scatter')

# Show plot
plt.show()

# Instruction2
# Change to make subplots based on study time
sns.relplot(x="absences", y="G3", data=student_data, kind="scatter", col='study_time')

# Show plot
plt.show()

# Instruction3
# Change this scatter plot to arrange the plots in rows instead of columns
sns.relplot(x="absences", y="G3",  data=student_data, kind="scatter", row="study_time")

# Show plot
plt.show()
