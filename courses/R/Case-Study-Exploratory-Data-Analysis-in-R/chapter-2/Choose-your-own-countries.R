# Add three more countries to this list
countries <- c("United States", "United Kingdom", "France", "Japan", "Brazil", "India", "Yemen", "Uganda", "Turkey")

# Filtered by_year_country: filtered_countries
filtered_countries <- by_year_country %>%
  filter(country %in% countries)

# Line plot of % yes over time faceted by country
ggplot(filtered_countries, aes(year, percent_yes)) +
  geom_line() +
  facet_wrap(~ country, scales = "free_y")
