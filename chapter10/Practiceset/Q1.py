# Create a Class "Programmer" for strong information of few programmers working in Microsoft
class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("Prathamesh", 1200000, 416007)
print(p.name, p.salary, p.pin)