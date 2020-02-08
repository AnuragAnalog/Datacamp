# Reset the index of ts2 to ts1, and then use linear interpolation to fill in the NaNs: ts2_interp
ts2_interp = ts2.reindex(ts1.index).interpolate('linear')

# Compute the absolute difference of ts1 and ts2_interp: differences 
differences = ts1 - ts2_interp

# Generate and print summary statistics of the differences
print(differences.describe())
