# Base layers
m <- ggplot(mtcars.cyl, aes(x = cyl, y = wt.avg))

# Plot 1: Draw bar plot with geom_bar
m + geom_bar(stat = "identity", fill = "skyblue")

# Plot 2: Draw bar plot with geom_col
m + geom_col(fill = "skyblue")

# Plot 3: geom_col with variable widths.
m + geom_col(width = mtcars.cyl$prop, fill = "skyblue")
 
# Plot 4: Add error bars
m + 
  geom_col(stat = "identity", width = mtcars.cyl$prop) +
  geom_errorbar(aes(ymin = wt.avg - sd, ymax = wt.avg + sd), width = 0.1)
