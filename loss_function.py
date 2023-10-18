def mean_squared_error(predictions, targets):
    """
    Calculate the mean squared error between predictions and target values.

    Args:
        predictions (list or numpy array): Predicted values.
        targets (list or numpy array): Target values.

    Returns:
        float: Mean squared error.
    """
    if len(predictions) != len(targets):
        raise ValueError("Length of predictions and targets must be the same.")

    squared_errors = [(pred - target) ** 2 for pred, target in zip(predictions, targets)]
    mse = sum(squared_errors) / len(predictions)
    return mse

predictions = [1.5, 2.0, 2.5, 3.0]
targets = [1.0, 2.0, 2.5, 3.5]

# Calculate MSE
mse = mean_squared_error(predictions, targets)
print(f"Mean Squared Error: {mse}")