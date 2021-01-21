import numpy as np

def AND(x1, x2):
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b = -0.7
  tmp = np.sum(x*w) + b
  if tmp <= 0:
    return 0
  else:
    return 1

def NAND(x1, x2):
  x = np.array([x1, x2])
  w = np.array([-0.5, -0.5])
  b = 0.7
  tmp = np.sum(x*w) + b
  if tmp <= 0:
    return 0
  else:
    return 1
  
def OR(x1, x2):
  x = np.array([x1, x2])
  w = np.array([0.5, 0.5])
  b = -0.2
  tmp = np.sum(x*w) + b
  if tmp <= 0:
    return 0
  else:
    return 1
def XOR(x1, x2):
  w1 = NAND(x1, x2)
  w2 = OR(x1, x2)
  
  return AND(w1, w2)

def main():
  x1 = int(input("input x1:"))
  x2 = int(input("input x2:"))
  print()
  print(AND(x1,x2))
  print(NAND(x1,x2))
  print(OR(x1,x2))
  print(XOR(x1,x2))
  
if __name__ == '__main__':
    main()
