# Draw samples of waiting times: waiting_times
waiting_times = successive_poisson(764, 715, size=100000)

# Make the histogram
plt.hist(waiting_times, normed=True, bins=100, histtype='step')

# Label axes
plt.xlabel('Time')
plt.ylabel('Prob')

# Show the plot
plt.show()

