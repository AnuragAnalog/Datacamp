# Instruction1
# Import the plot_acf module from statsmodels
from statsmodels.graphics.tsaplots import plot_acf

# Plot 1: MA parameter = -0.9
plot_acf(simulated_data_1, lags=20)
plt.show()

# Instruction2
# Plot 2: MA parameter = 0.9
plot_acf(simulated_data_2, lags=20)
plt.show()

# Instruction3
# Plot 3: MA parameter = -0.3
plot_acf(simulated_data_3, lags=20)
plt.show()
