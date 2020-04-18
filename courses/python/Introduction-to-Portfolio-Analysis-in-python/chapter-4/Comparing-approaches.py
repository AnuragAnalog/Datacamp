# Instruction1
# Print the weights of both portfolios types
print(cleaned_weights_maxsharpe, cleaned_weights_maxsharpe_EW, sep="\n")

# Instruction2
# Print the performance of both portfolios types
perf_max_sharpe = ef.portfolio_performance(verbose=True)
perf_max_sharpe_EW = ef_2.portfolio_performance(verbose=True)
