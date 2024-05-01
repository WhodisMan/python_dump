

def disarium_check(n):
    lst = [int(x) for x in str(n)]
    temp = 0
    for i in range(len(lst)):
        temp += (lst[i] ** (i+1))

    return temp == n

# ans = not disarium_check(136)
# print(f"{ans * 'NOT '}Disarium number")


def generator(n):
    for i in range(n):
        if disarium_check(i):
            print(i)

print("Generator ")
generator(10000)