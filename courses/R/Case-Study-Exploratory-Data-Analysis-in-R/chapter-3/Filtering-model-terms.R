# Print the country_coefficients dataset
print(country_coefficients)

# Filter for only the slope terms
country_coefficients %>%
  filter(term == "year")
