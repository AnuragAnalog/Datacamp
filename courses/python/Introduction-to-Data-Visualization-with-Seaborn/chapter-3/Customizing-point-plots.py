# Instruction1
# Create a point plot of family relationship vs. absences
sns.catplot(x='famrel', y='absences', data=student_data, kind='point')
            
# Show plot
plt.show()

# Instruction2
# Add caps to the confidence interval
sns.catplot(x="famrel", y="absences", data=student_data, kind="point", capsize=0.2)
        
# Show plot
plt.show()

# Instruction3
# Remove the lines joining the points
sns.catplot(x="famrel", y="absences", data=student_data, kind="point", capsize=0.2, join=False)
            
# Show plot
plt.show()
