# Instruction1
# Set the index to datetime
returns_sp500.index=pd.to_datetime(returns_sp500.index)

# Instruction2
# Set the index to datetime
returns_sp500.index=pd.to_datetime(returns_sp500.index)

# Ensure the returns are a series
returns=pd.Series(returns_sp500['S&P500'])

# Check the type
print(type(returns))

# Instruction3
# Set the index to datetime
returns_sp500.index=pd.to_datetime(returns_sp500.index)

# Ensure the returns are a series
returns=returns_sp500['S&P500']

# Create the returns tear sheet
fig = pf.create_returns_tear_sheet(returns, return_fig=True)

# Display a zoomed in version of the tear sheet
display_tear_sheet()
