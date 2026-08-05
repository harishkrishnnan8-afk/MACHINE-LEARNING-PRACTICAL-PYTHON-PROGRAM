import numpy as np

# Sigmoid Activation Function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Input dataset (XOR Logic Gate)
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([[0], [1], [1], [0]])

np.random.seed(42)
input_neurons = 2
hidden_neurons = 2
output_neurons = 1

# Weight and Bias Initialization
wh = np.random.uniform(size=(input_neurons, hidden_neurons))
bh = np.random.uniform(size=(1, hidden_neurons))
wout = np.random.uniform(size=(hidden_neurons, output_neurons))
bout = np.random.uniform(size=(1, output_neurons))

learning_rate = 0.5
epochs = 10000

# Training using Backpropagation
for epoch in range(epochs):
    # Forward Propagation
    hidden_layer_input = np.dot(X, wh) + bh
    hidden_layer_activations = sigmoid(hidden_layer_input)
    output_layer_input = np.dot(hidden_layer_activations, wout) + bout
    output = sigmoid(output_layer_input)

    # Backpropagation
    error = y - output
    slope_output_layer = sigmoid_derivative(output)
    slope_hidden_layer = sigmoid_derivative(hidden_layer_activations)

    d_output = error * slope_output_layer
    error_hidden_layer = d_output.dot(wout.T)
    d_hidden_layer = error_hidden_layer * slope_hidden_layer

    # Updating Weights and Biases
    wout += hidden_layer_activations.T.dot(d_output) * learning_rate
    bout += np.sum(d_output, axis=0, keepdims=True) * learning_rate
    wh += X.T.dot(d_hidden_layer) * learning_rate
    bh += np.sum(d_hidden_layer, axis=0, keepdims=True) * learning_rate

print("Actual Output:")
print(y.ravel())
print("\nPredicted Output after Backpropagation Training:")
print(np.round(output.ravel(), 4))
