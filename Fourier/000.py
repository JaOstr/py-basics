import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0, 1, 1000)
f1 = np.sin(2 * np.pi * x)
f2 = np.sin(4 * np.pi * x)
f3 = np.sin(6 * np.pi * x)
sum = f1 + f2 + f3

plt.plot(x, f1, linewidth = 0.5)
plt.plot(x, f2, linewidth = 0.5)
plt.plot(x, f3, linewidth = 0.5)
plt.plot(x, sum, linewidth = 1.2, color = 'red')
plt.show()
