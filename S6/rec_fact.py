# factorial of a number using recursion

def fact(n):
    if n == 0:
        return 1
    elif n < 0:
        return "Undefined"
    return n * fact(n - 1)



while True:
    num = (input("Enter a number : "))
    if num.lower() in ["quit","q"]:
        print("Bye")
        break
    print(f"Factorial of {num} = {fact(int(num))}")