library(gapminder)
library(dplyr)

# Summarize to find the median life expectancy
gapminder %>% summarize(medianLifeExp = median(lifeExp))
