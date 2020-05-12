# Create airline_totals_sorted
airline_totals_sorted = airline_totals.sort_values(by='bumps_per_10k', ascending=False)

# Print airline_totals_sorted
print(airline_totals_sorted)

# Save as airline_totals_sorted.csv
airline_totals_sorted.to_csv('airline_totals_sorted.csv')
