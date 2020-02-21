# Extract temperature data for August: august
august = df.Temperature.loc['2010-08-01':'2010-08-31']

# Downsample to obtain only the daily highest temperatures in August: august_highs
august_highs = august.resample('D').max()

# Extract temperature data for February: february
february = df.Temperature.loc['2010-02-01':'2010-02-28']

# Downsample to obtain the daily lowest temperatures in February: february_lows
february_lows = february.resample('D').min()
