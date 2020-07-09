# Basic ggplot() command, coded for you
p <- ggplot(mtcars, aes(x = wt, y = hp, col = am)) + geom_point() + geom_smooth()

# Add scale_x_continuous()
p + scale_x_continuous(limits = c(3, 6), expand = c(0, 0))

# Add coord_cartesian(): the proper way to zoom in
p + coord_cartesian(xlim = c(3, 6))

