# Downsample to 6 hour data and aggregate by mean: df1
df1 = df.Temperature.resample("6H").mean()

# Downsample to daily data and count the number of data points: df2
df2 = df.Temperature.resample("D").count()
