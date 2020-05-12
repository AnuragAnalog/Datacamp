# Instruction1
# Model setup
model = RandomForestClassifier(n_estimators=5, max_depth=20)

# Model fitting
model.fit(X_train, y_train)

# Testing on training data
test_and_show_accuracy(model,
                       X_test=X_train, 
                       y_test=y_train)

# Instruction2
# Model setup
model = RandomForestClassifier(n_estimators=5, max_depth=20)

# Model fitting
model.fit(X_train, y_train)

# Testing on testing data
test_and_show_accuracy(model,
                       X_test=X_test, 
                       y_test=y_test)
