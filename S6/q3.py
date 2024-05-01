s = input()

for i in s:
    if i.lower() in ['a', 'e', 'i', 'o', 'u']:
        print(i * 2, end='')
    else:
        print(i, end='')
