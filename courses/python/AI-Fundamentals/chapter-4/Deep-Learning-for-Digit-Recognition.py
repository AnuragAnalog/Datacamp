# Instruction1
# Construct the Deep Neural Network
deep_net = make_deep_net(input_shape=[28, 28, 1],
                         n_output_classes=10)

# Instruction2
# Construct the Deep Neural Network
deep_net = make_deep_net(input_shape=[28, 28, 1],
                         n_output_classes=10)

# Train the Deep Neural Network
deep_net.fit(x=x_train, y=y_train,
          	  validation_data=(x_test, y_test),
          	  batch_size=128,
          	  epochs=1)

# Instruction3
# Construct the Deep Neural Network
deep_net = make_deep_net(input_shape=[28, 28, 1],
                         n_output_classes=10)

# Train the Deep Neural Network
deep_net.fit(x=x_train, y=y_train,
          	 validation_data=(x_test, y_test),
          	 batch_size=128,
          	 epochs=1)

# Estimate the network performance
evaluate_deep_net(deep_net, x=x_test, y=y_test)

# Instruction4
# Construct the Deep Neural Network
deep_net = make_deep_net(input_shape=[28, 28, 1],
                         n_output_classes=10)

# Train the Deep Neural Network
deep_net.fit(x=x_train, y=y_train,
          	 validation_data=(x_test, y_test),
          	 batch_size=128,
          	 epochs=3)

# Estimate the network performance
evaluate_deep_net(deep_net, x=x_test, y=y_test)
