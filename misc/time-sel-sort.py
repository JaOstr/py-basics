from matplotlib import pyplot as plt
import timeit
import random

size = list(range(1, 101))
time = [0] * 100

def selection_sort(a):
    for i in range(len(a) - 1):
        minIdx = i
        for j in range(i+1, len(a)):
            if a[j] < a[minIdx]:
                minIdx = j
        a[i], a[minIdx] = a[minIdx], a[i]

random.seed()

for i in range(len(size)):
    a =  [random.randint(1, size[i]) for _ in range(size[i])]
    time[i] = timeit.timeit('selection_sort(a)', globals = globals(), number=1000)

plt.plot(size, time)
plt.show()
