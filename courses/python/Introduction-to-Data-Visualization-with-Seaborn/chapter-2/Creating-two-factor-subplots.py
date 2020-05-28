# Instruction1
# Create a scatter plot of G1 vs. G3
sns.relplot(x='G1', y='G3', data=student_data, kind='scatter')

# Show plot
plt.show()

# Instruction2
# Adjust to add subplots based on school support
sns.relplot(x="G1", y="G3", data=student_data, kind="scatter", col='schoolsup', col_order=['yes', 'no'])

# Show plot
plt.show()

# Instruction3
# Adjust further to add subplots based on family support
sns.relplot(x="G1", y="G3", 
            data=student_data,
            kind="scatter", 
            col="schoolsup",
            col_order=["yes", "no"],
            row='famsup',
            row_order=['yes', 'no'])

# Show plot
plt.show()
