# Original plot, color provided
z
myRed

# Extend z with theme() function and 3 args
z +
  theme(strip.text = element_text(size = 16, color = myRed),
        axis.title = element_text(hjust = 0, color = myRed, face = "italic"),
        axis.text = element_text(color = "black"))
