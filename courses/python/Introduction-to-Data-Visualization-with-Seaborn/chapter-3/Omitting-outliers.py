# Create a box plot with subgroups and omit the outliers
sns.catplot(x='internet', y='G3', data=student_data, kind='box', hue='location', sym="")

# Show plot
plt.show()
