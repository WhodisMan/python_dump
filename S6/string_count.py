# Count uppercase and lowercase in a string

def counter(string):
    upper = 0
    u_list = []
    lower = 0
    l_list = []
    idk_man = 0
    idk_man_list =[]
    for x in string:
        if x.isupper():
            upper += 1
            u_list.append(x)
        elif x.islower():
            lower += 1
            l_list.append(x)
        else:
            idk_man += 1
            idk_man_list.append(x)

    print(f"Upper case count = {upper} {u_list}\nLower case count = {lower} {l_list}\nIDK MAN count = {idk_man} {idk_man_list}")


while True:
    string = input("Enter a string : ")
    if string.lower() in ["quit", "q", "0"]:
        print("Bye")
        break
    counter(string)

