class employee:

    def __init__(self, id, name, salary):
        self.empid = id
        self.empname = name
        self.empsalary = salary

    def displaydetails(self):

        print(f"{self.empid}\t{self.empname}        {self.empsalary}")



a = employee(2422, "ABC", 57000)
b = employee(2423, "DEF", 62000)

print("ID      Name       Salary")
a.displaydetails()
b.displaydetails()
