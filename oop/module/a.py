def pow(a, b):
    ans = 1
    while b > 0:
        ans *= a
        b -= 1
    return ans


print pow(-1, -1)
1/0