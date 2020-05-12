# Initialize the model
model = Sequential()

# Create your 5-layer network (input specified implicitly with 1st layer)
model.add(Conv2D(filters=64, kernel_size=(3, 3), input_shape=(28, 28, 1)))
model.add(MaxPooling2D())
model.add(Flatten())
model.add(Dense(units=10, activation='softmax'))

# Set fitting hyper-parameters and compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
