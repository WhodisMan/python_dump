# armstrong number in an interval

def armstrong_check(n):
    temp = 0
    digits = len(n)
    for i in n:
        temp += int(i) ** digits
    return temp == int(n)


a = int(input("Enter lower range : "))
b = int(input("Enter upper range : "))
for j in range(a, b):
    if armstrong_check(str(j)):
        print(j)
