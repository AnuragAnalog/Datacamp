# Draw a bar plot of cyl, filled according to am
ggplot(mtcars, aes(x = cyl, fill = am)) + geom_bar()

# Change the position argument to stack
ggplot(mtcars, aes(x = cyl, fill = am)) + geom_bar(position = 'stack')

# Change the position argument to fill
ggplot(mtcars, aes(x = cyl, fill = am)) + geom_bar(position = 'fill')

# Change the position argument to dodge
ggplot(mtcars, aes(x = cyl, fill = am)) + geom_bar(position = 'dodge')

