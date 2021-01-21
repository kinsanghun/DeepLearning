import numpy as np
import matplotlib.pylab as plt

def step_func(x):
  y = x > 0
  return y.astype(np.int)

def sigmoid(x):
  return 1 / (1 + np.exp(-x))


x = np.arange(-5.0, 5.0, 0.1)

# step_function
y = step_func(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()

# sigmoid_function
y = step_func(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()
