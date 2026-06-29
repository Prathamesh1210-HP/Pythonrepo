class Employee:
    def __init__(self):
        print("Constructor of Em")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Emp")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Employee")
    c = 3

# o = Employee()
# print(o.a)
# # print(o.b) Shows an error as there is no b attribute in employee class

# o = Programmer()
# print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)