def evaluate_deep_net(model, x_test, y_test):
    # Generate the test predictions and evaluate against the ground truth
    score = model.evaluate(x=x_test, y=y_test)
    # Print the evaluation results in a human readable form
    print('Test loss: %.2f' % score[0])
    print('Test accuracy: %.2f %%' % (100*score[1]))
