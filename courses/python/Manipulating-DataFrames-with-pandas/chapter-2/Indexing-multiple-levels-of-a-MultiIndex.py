# Look up data for NY in month 1 in sales: NY_month1
NY_month1 = sales.loc['NY', 1]

# Look up data for CA and TX in month 2: CA_TX_month2
CA_TX_month2 = sales.loc[[('CA', 2), ('TX', 2)]]

# Access the inner month index and look up data for all states in month 2: all_month2
all_month2 = sales.loc[[('CA', 2), ('NY', 2), ('TX', 2)]]
