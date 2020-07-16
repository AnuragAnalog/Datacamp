library(gapminder)
library(dplyr)

# Sort in ascending order of lifeExp
gapminder %>% arrange(lifeExp)
  
# Sort in descending order of lifeExp
gapminder %>% arrange(desc(lifeExp))

