def min_coins(amount):
    _1 = 0
    _2 = 0
    _5 = 0

    if amount == 1:
        _1 = 1
    elif amount == 2:
        _1 = 2
    elif amount == 3:
        _1 = 1
        _2 = 1
    else:
        t1 = int((amount - 4) / 5)
        t2 = (amount - 4) % 5

        _5 = t1

        if t2 % 2 == 0:
            _1 = 2
        else:
            _1 = 1

        if t2 in [0]:
            _2 = 1
        elif t2 in [1, 2]:
            _2 = 2
        elif t2 in [3, 4]:
            _2 = 3

    print(f"5 coins : {_5}\n2 coins : {_2}\n1 coins : {_1}\n")


while 1:
    n = int(input("Enter amount : "))
    min_coins(n)
    if n == 0:
        exit()
