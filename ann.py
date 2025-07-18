import numpy as np

def tanh(x):
    return np.tanh(x)


w1 = np.random.uniform(-0.5, 0.5)
w2 = np.random.uniform(-0.5, 0.5)
w3 = np.random.uniform(-0.5, 0.5)
w4 = np.random.uniform(-0.5, 0.5)
w5 = np.random.uniform(-0.5, 0.5)
w6 = np.random.uniform(-0.5, 0.5)

b1 = 0.5
b2 = 0.7

x1 = 0.6  
x2 = -0.8  

h1 = tanh(w1 * x1 + w2 * x2 + b1)
h2 = tanh(w3 * x1 + w4 * x2 + b1)

y = tanh(w5 * h1 + w6 * h2 + b2)

print(f"Weights: {w1}, {w2}, {w3}, {w4}, {w5}, {w6}")
print(f"Hidden Layer Outputs: h1={h1}, h2={h2}")
print(f"Final Output: y={y}")
