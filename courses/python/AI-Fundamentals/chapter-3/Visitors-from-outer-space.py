# Instruction1
# Add outliers to the blob
X_new, outliers = add_outliers(X_raw,
							   outlier_distance=200,
                               n_outliers=5)

plot_3d_data(X_new, outliers)

# Instruction2
# Add outliers to the blob
X_new, outliers = add_outliers(X_raw, outlier_distance=200, n_outliers=5)

plot_3d_data(X_new, outliers)  

# Extract principal components
X_2D, outliers_2D = extract_components(X_new, outliers, n_components=2)

# Plot the PCA results
plot_2d_data(X_2D, outliers_2D)
