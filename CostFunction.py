import numpy as np
import matplotlib.pyplot as plt


def cost_function(x, y):
    ypred = 0*x+0  # m*x + b
    m = len(x)
    j = 1/(2*m)*np.sum(np.dot(ypred-y, ypred-y))
    return j


x = np.array([1, 2, 3, 4, 5])  # Your data (x)
y = np.array([2, 3, 5, 6, 8])  # Targrt of data (x)

result = cost_function(x, y)
print(f"Your Error {result}")

plt.scatter(x, y, c='r')
plt.xlabel("x")
plt.ylabel("y")
plt.show()
