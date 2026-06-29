class Employee:
    language = "Py" # This is a class attribute
    salary = 1400000

    def __init__(self, name, salary, language): # dunder method which's automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I'm creating an object.")

    def getinfo(self):
        print(f"The lanuage is {self.language}. The salary is {self.salary}")
   
    @staticmethod # There's no need to get self as argument when it declared as @staticmethod 
    def greet():
        print("Good afternoon!")

Patu = Employee("Patu", 1300000, "JavaScript")
 # This is an instance attribute
Patu.getinfo()