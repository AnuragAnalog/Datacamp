# Scatter plot: carat (x), price (y), clarity (color)
ggplot(diamonds, aes(carat, price, color = clarity)) + geom_point()

# Adjust for overplotting
ggplot(diamonds, aes(carat, price, color = clarity)) + geom_point(alpha = 0.5)

# Scatter plot: clarity (x), carat (y), price (color)
ggplot(diamonds, aes(clarity, carat, color = price)) + geom_point(alpha = 0.5)

# Dot plot with jittering
ggplot(diamonds, aes(clarity, carat, color = price)) + geom_point(alpha = 0.5, position = 'jitter')

