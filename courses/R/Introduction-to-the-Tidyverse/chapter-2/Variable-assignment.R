# Load the ggplot2 package as well
library(gapminder)
library(ggplot2)
library(dplyr)

# Create gapminder_1952
gapminder_1952 <- gapminder %>% filter(year == 1952)
