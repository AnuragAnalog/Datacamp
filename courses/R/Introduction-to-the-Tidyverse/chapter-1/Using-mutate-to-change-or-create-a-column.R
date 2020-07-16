library(gapminder)
library(dplyr)

# Use mutate to change lifeExp to be in months
gapminder %>% mutate(lifeExp = 12 * lifeExp)

# Use mutate to create a new column called lifeExpMonths
gapminder %>% mutate(lifeExpMonths = 12 * lifeExp)
