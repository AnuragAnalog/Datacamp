# Get the minimum risk portfolio for a target return 
weights = ef.efficient_return(0.2)
print(weights)

# Show portfolio performance 
ef.portfolio_performance(verbose=True, risk_free_rate=0.1)
