# Define your model
model = RandomForestClassifier()

# Divide the data into the training and testing set and train the model
X_train, X_test, y_train, y_test = train_test_split(client_data, client_churned)
model.fit(X_train, y_train)

# Generate predictions on the test set
predictions_test = model.predict(X_test)

# Evaluate the model predictions using metrics appropriate for this problem class
print_metrics(target_test=y_test,
              predictions=predictions_test, 
              metrics=['accuracy', 'precision', 'recall'])
