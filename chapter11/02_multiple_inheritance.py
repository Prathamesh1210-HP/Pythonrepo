# Multiple Inheritance

class Employee:
    company = "ITC"
    def show(self):
        print(f"The name is {self.company} and the salary is {self.company}")

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all the languages here is youe language: {self.language}")

class Programmmer(Employee, Coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language.")

a = Employee()
b = Programmmer()

b.show()
b.printLanguage()
b.showLanguage()

print(b.company, b.language)