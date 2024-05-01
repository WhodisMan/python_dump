def round(n):
    a = (n // 10) * 10
    b = a + 10
    return b if n - a >= b - n else a


t = int(input())
for i in range(t):
    x = int(input())
    print(100 - round(x))
