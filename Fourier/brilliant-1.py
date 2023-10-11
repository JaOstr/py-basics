import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-0.1, 1.1, 10000)
y = x * (1 - x)

def u(n):
    f = 1/6 + x * 0
    for i in range(1, n+1):
        f -= (1/(np.pi**2)) * (1/(i**2)) * np.cos(2*np.pi*i*x)
    return f

mng = plt.get_current_fig_manager()
mng.full_screen_toggle()
for i in range(11):
    f = u(i)
    plt.plot(x, y)
    plt.plot(x, f)
    plt.show()
