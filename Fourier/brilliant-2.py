import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-0.1, 1.1, 10000)
y = np.array([1 if n <= 5000 else -1 for n in range(10000)])

def u(n):
    f = x * 0
    for i in range(1, n+1):
        f += (2 * (1 - (-1)**i) / np.pi / i) * np.sin(2 * np.pi * i * x)
    return f

for i in range(40, 50, 2):
    f = u(i)
    plt.plot(x, y)
    plt.plot(x, f)
    plt.show()
