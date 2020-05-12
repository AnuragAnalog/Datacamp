# Instruction1
# Select the appropriate method to call the model training procedure
linear_model.fit(X=x_train, y=y_train)

# Check the "goodness-of-fit" of the fitted model
check_model_fit(model=linear_model,
                x=x_train,
                y=y_train)

# Instruction2
# Create a new dataset x2_train with 2nd degree polynomial features.
poly = PolynomialFeatures(degree=2)
x2_train = poly.fit_transform(x_train)

# Fit the linear model using the newly created dataset
linear_model.fit(X=x2_train, y=y_train)

# Check the "goodness-of-fit" of the fitted model  
check_model_fit(model=linear_model,
                x=x2_train,
                y=y_train)
