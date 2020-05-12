# Select the model appropriate for the task
model = DecisionTreeClassifier()

# Train the model
model.fit(X=X_train, y=y_train)

# Generate predictions
prediction_results = model.predict(X=X_test) 

# Test the model
evaluate_predictions(y_true=y_test,
                     y_pred=prediction_results)
