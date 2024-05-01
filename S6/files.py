f = open("1.txt","w+")

f.write("hello\n hello there\n how are you\n all good foo\n ez pz")


f.close()

f = open("2.txt","x")
f.close()

# write a python program to read a file line by line and store it into a list

lst = []
def q1():
    f = open("1.txt","r+")

    lst=[]
    str = f.read()
    lst = str.split("\n")
    print(lst)

    # while str:
    #     lst.append(str)
    #     str = f.readline()
    #     print(str)

    f.close()
q1()

# python program to copy odd line of one file to another

 