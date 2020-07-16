library(gapminder)
library(dplyr)

# Find median life expectancy and maximum GDP per capita in each continent/year combination
gapminder %>% group_by(year, continent) %>% summarize(medianLifeExp = median(lifeExp), maxGdpPercap = max(gdpPercap))
