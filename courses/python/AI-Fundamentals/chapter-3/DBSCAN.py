# Instruction1
# Set eps to 0.1
eps = 0.1

dbscan.set_params(eps=eps)

clusters = dbscan.fit_predict(X)

plot_clusters(X, clusters)

# Instruction2
# Set eps to 0.5
eps = 0.5

dbscan.set_params(eps=eps)

clusters = dbscan.fit_predict(X)

plot_clusters(X, clusters)

# Instruction3
# Set eps to 2
eps = 2

dbscan.set_params(eps=eps)

clusters = dbscan.fit_predict(X)

plot_clusters(X, clusters)
