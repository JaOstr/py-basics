def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i in range(len(a)):
        for j in range(len(b)):
            c[i+j] += a[i] * b[j]
    return c

print(mul([2, 3, 1], [1, 0, 2]))
