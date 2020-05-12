# Instruction1
# Generate data comprising of the "clean" and "noisy" components
noisy_data, true_labels = make_fake_data(n_blobs=2, n_inliers=1000, n_outliers=50)

# Detect anomalies
predicted_anomalies = isolation_forest.fit_predict(noisy_data)
    
# Plot results    
plot_detected_anomalies(noisy_data, true_labels, predicted_anomalies)

# Instruction2
# Generate data comprising of the "clean" and "noisy" components
noisy_data, true_labels = make_fake_data(n_blobs=2, n_inliers=1000, n_outliers=50)

# Detect anomalies
predicted_anomalies = isolation_forest.fit_predict(noisy_data)
    
# Plot results    
plot_detected_anomalies(noisy_data, true_labels, predicted_anomalies)

# Instruction3
# Generate data comprising of the "clean" and "noisy" components
noisy_data, true_labels = make_fake_data(n_blobs=2, n_inliers=1000, n_outliers=50)

# Detect anomalies
predicted_anomalies = isolation_forest.fit_predict(noisy_data)
    
# Plot results    
plot_detected_anomalies(noisy_data, true_labels, predicted_anomalies)
