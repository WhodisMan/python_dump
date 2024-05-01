import random

a = [26,28,38,1,5]

while True:
    random.shuffle(a)
    print(a)
    flag = 0
    for i in range(len(a) - 1):
        if a[i] <= a[i + 1]:
            flag = 1
        else:
            flag = 0
            break
    if flag == 1:
        break

