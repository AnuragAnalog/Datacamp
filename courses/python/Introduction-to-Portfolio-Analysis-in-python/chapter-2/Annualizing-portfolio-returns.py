# Instruction1
# Calculate total rate of return from portfolio AUM
total_return = (pf_AUM[-1] - pf_AUM[0]) / pf_AUM[0]

# Instruction2
# Calculate total rate of return from start to end
total_return = (pf_AUM[-1] - pf_AUM[0]) / pf_AUM[0]

# Annualize return
annualized_return = ((1 + total_return)**(12/months))-1
print (annualized_return)
