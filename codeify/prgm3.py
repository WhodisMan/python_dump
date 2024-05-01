
[n, cb, cp] = list(map(int, input().split()))
amt = 0
for i in range(n):
    [bi, pi] = list(map(int, input().split()))

    if bi % 10 != 0:
        bi = bi // 10 * 10 + 10
    if pi % 10 != 0:
        pi = pi // 10 * 10 + 10

    bi = int(bi/10)
    pi = int(pi/10)

    amt = amt + cb*bi + cp*pi

print(amt)






