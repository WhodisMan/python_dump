def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


n = 0
while True:
    n = int(input("Enter number : "))
    if n <=0 : break
    print(fact(n))
