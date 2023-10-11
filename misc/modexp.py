def exp(x, y, m):
    mod = x % m
    res = 1
    while y > 0:
        if y % 2 == 1:
            res = (res * mod) % m
        mod = (mod * mod) % m
        y //= 2
    
    return res


print(exp(5, 117, 19))
