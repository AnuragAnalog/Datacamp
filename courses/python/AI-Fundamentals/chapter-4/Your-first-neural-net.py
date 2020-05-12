# Initialize the model
model = Sequential()

# Add the hidden and the output layer, specify the layer type, number of units and input/output dimensions
model.add(Dense(units=8, input_dim=16, activation='relu'))
model.add(Dense(units=4, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
