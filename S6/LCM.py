# def find_lcm(x, y):
#     larger = [x if x > y else y][0]
#
#     while (larger % x) != 0 or (larger % y) != 0:
#         larger += 1
#     lcm = larger
#
#     return lcm
#




def find_lcm(x, y):
    l1 = [x * i for i in range(1,y+1)]
    l2 = [y * i for i in range(1,x+1)]

    lcm = [x for x in l1 if x in l2][0]

    return lcm


