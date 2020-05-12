# Instruction1
# Define the model
model = LogisticRegression(C=0.000001)

# Fit the model
model.fit(training_inputs, training_labels)

# Check model performance
check_performance(model, testing_inputs, testing_labels)

# Instruction2
# Define the model
model = LogisticRegression(C=0.0001)

# Fit the model
model.fit(training_inputs, training_labels)

# Check model performance
check_performance(model, testing_inputs, testing_labels)

# Instruction3
# Define the model
model = LogisticRegression(C=0.01)

# Fit the model
model.fit(training_inputs, training_labels)

# Check model performance
check_performance(model, testing_inputs, testing_labels)

# Instruction4
# Define the model
model = LogisticRegression(C=100)

# Fit the model
model.fit(training_inputs, training_labels)

# Check model performance
check_performance(model, testing_inputs, testing_labels)
