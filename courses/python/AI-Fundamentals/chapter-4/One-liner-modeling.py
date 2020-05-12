def make_deep_net(input_shape, n_output_classes, n_kernels=32, kernel_size=(3, 3)):
    # Initialize the sequential model
    model = Sequential()	
    # Add the convolutional layer (containing implicitly the input layer)
    model.add(Conv2D(input_shape=input_shape, filters=n_kernels, kernel_size=kernel_size, activation='relu'))
    # Add the flattening layer
    model.add(Flatten())	
    # Add the fully connected layer
    model.add(Dense(n_output_classes, activation='softmax')) 
    # Compile the model
    model.compile(optimizer='adam', metrics=['accuracy'], loss='categorical_crossentropy')
    
    return model
