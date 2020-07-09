# Define a hexadecimal color
my_color <- "#4ABEFF"

# Draw a scatter plot with color *aesthetic*
ggplot(mtcars, aes(wt, mpg, col = cyl)) + geom_point()

# Same, but set color *attribute* in geom layer 
ggplot(mtcars, aes(wt, mpg)) + geom_point(col = my_color)

# Set the fill aesthetic; color, size and shape attributes
ggplot(mtcars, aes(wt, mpg, fill = cyl)) + geom_point(size = 10, shape = 23, color = my_color)
