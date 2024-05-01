stu_marks = {"jenny": 92, "haryy": 78, "denil": 56, "rahul": 41, "ankit": 99, "anu": 34}

for i in stu_marks:
    marks = stu_marks[i]

    if 100 >= marks >= 91:
        grade = "A+"
    elif 90 >= marks >= 81:
        grade = "A"
    elif 80 >= marks >= 71:
        grade = "B+"
    elif 70 >= marks >= 61:
        grade = "B"
    elif 60 >= marks >= 51:
        grade = "C"
    elif 50 >= marks >= 41:
        grade = "D"
    else:
        grade = "F"

    print(f"{i} : {stu_marks[i]} : {grade}")
    stu_marks[i] = [stu_marks[i], grade]
print(stu_marks)

print(stu_marks["anu"][0])
