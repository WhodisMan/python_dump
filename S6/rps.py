import random

run = 1
cscore = 0
uscore = 0
while run:
    dict = {"r": -1, "p": 0.5, "s": 2}
    fangi = {"r": "Rock", "p": "Paper", "s": "Scissor"}

    choices = ["r", "p", "s"]
    comp = random.choice(choices)
    user = input("Enter choice : {r/p/s} : ").lower()
    while user not in choices:
        user = input("Enter choice : {r/p/s} : ").lower()

    p1 = dict[user] / dict[comp]
    p2 = dict[comp] / dict[user]

    if p1 == p2:
        result = "Draw"
    else:
        if p1 > p2:
            result = "User Winner"
            uscore += 1
        else:
            result = "Computer Winner"
            cscore += 1

    print(
        f"Computer : {fangi[comp]}        User : {fangi[user]}\nResult : {result}\nScore : Computer : {cscore}      user : {uscore}\n")
