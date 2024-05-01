def find_hcf(x, y):
    smaller = [x if x < y else y][0]
    hcf = 1

    for i in range(1, smaller + 1):
        if (x % i) == 0 and (y % i) == 0:
            hcf = i

    return hcf


# def find_hcf(x, y):
#     l1 = [i for i in range(1, x + 1) if x % i == 0]
#     l2 = [i for i in range(1, y + 1) if y % i == 0]
#
#     hcf = [x for x in l1 if x in l2][-1]
#
#     return hcf

print(find_hcf(1024,250))
