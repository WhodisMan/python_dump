def prime():
    flag = 0
    for i in range(2, int(n * 0.5)):
        if n % i == 0:
            flag = 1
    return not flag


n = 0
while n != -1:
    n = int(input("Enter a number : "))
    print(f"PRIME {prime()}")




for n in range(2,100):
    flag = 0
    for i in range(2,int(n/2)+1):
        if(n%i) == 0:
            flag=1
            break

    print(f"{n} >>> {flag*'NOT '}PRIME")