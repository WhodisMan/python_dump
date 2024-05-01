
for i in range(100):
    if i % 3 == 0 and i % 5 == 0:
        result = "FizzBuzz"
    elif i % 5 == 0:
        result = "Buzz"
    elif i % 3 == 0:
        result = "Fizz"
    else:
        result = i
    print(f"{i} >>> {result}")