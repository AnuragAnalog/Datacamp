# Subset for Egypt to India
temp_by_country_city_vs_year.loc['Egypt':'India']

# Subset for Egypt, Cairo to India, Delhi
temp_by_country_city_vs_year.loc[('Egypt', 'Cairo'):('India', 'Delhi')]

# Subset in both directions at once
temp_by_country_city_vs_year.loc[('Egypt', 'Cairo'):('India', 'Delhi'), 2005:2010]
