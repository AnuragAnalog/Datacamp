
# Create box plot with Seaborn's default settings
_ = sns.boxplot(x='species', y='petal length (cm)', data=df)

# Label the axes
plt.xlabel("species")
plt.ylabel("petal length(cm)")


# Show the plot
plt.show()

