library(gapminder)
library(dplyr)

# Filter for China in 2002
gapminder %>% filter(year == 2002, country == "China")
