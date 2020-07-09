# Basic scatter plot: wt on x-axis and mpg on y-axis; map cyl to col
ggplot(mtcars, aes(wt, mpg, color = cyl)) + geom_point(size = 4)

# Hollow circles - an improvement
ggplot(mtcars, aes(wt, mpg, color = cyl)) + geom_point(size = 4, shape = 1)

# Add transparency - very nice
ggplot(mtcars, aes(wt, mpg, color = cyl)) + geom_point(size = 4, alpha = 0.6)

