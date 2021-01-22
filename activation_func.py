import numpy as np
import matplotlib.pylab as plt

def step_func(x):
  y = x > 0
  return y.astype(np.int)

def sigmoid(x):
  return 1 / (1 + np.exp(-x))

#Main use
def relu(x):
  return np.maximum(0, x)

def softmax(x):
  c = np.max(x) # 가장 큰 값 찾기
  exp_x = np.exp(x - c)
  sum_exp_x = np.sum(exp_x)
  y = exp_x / sum_exp_x
  
  return y


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
