# A basic histogram, add coloring defined by cyl
ggplot(mtcars, aes(mpg, fill = cyl)) +
  geom_histogram(binwidth = 1)

# Change position to identity
ggplot(mtcars, aes(mpg, fill = cyl)) +
  geom_histogram(binwidth = 1, position = 'identity')

# Change geom to freqpoly (position is identity by default)
ggplot(mtcars, aes(mpg, color = cyl)) + geom_freqpoly(binwidth = 1)
