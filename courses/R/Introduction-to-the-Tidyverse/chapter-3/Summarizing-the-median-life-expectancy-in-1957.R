library(gapminder)
library(dplyr)

# Filter for 1957 then summarize the median life expectancy
gapminder %>% filter(year == 1957) %>% summarize(medianLifeExp = median(lifeExp))
