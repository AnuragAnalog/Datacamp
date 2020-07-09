library(grid)
# Increase spacing between facets
z +
  theme(panel.spacing.x = unit(2, "cm"))

# Adjust the plot margin
z +
  theme(panel.spacing.x = unit(2, "cm"), plot.margin = unit(c(1, 2, 1, 1), "cm"))
