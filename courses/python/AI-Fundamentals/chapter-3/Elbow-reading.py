# Instruction1
k_range = list(range(2, 6))

summed_distances = []

for k in k_range:    
    kmeans.set_params(n_clusters=k).fit(X)
    summed_distances.append(kmeans.inertia_)

plot_elbow_curve(k_range, summed_distances)
