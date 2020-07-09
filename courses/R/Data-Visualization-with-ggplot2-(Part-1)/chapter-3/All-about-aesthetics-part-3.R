# Map cyl to size
ggplot(mtcars, aes(wt, mpg, size = cyl)) + geom_point()

# Map cyl to alpha
ggplot(mtcars, aes(wt, mpg, alpha = cyl)) + geom_point()

# Map cyl to shape 
ggplot(mtcars, aes(wt, mpg, shape = cyl)) + geom_point()

# Map cyl to label
ggplot(mtcars, aes(wt, mpg, label = cyl)) + geom_text()

