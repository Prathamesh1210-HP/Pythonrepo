class Employee:
    language = "Py" # This is a class attribute
    salary = 1400000

    def getinfo(self):
        print(f"The lanuage is {self.language}. The salary is {self.salary}")
   
    @staticmethod # There's no need to get self as argument when it declared as @staticmethod 
    def greet():
        print("Good afternoon!")

Patu = Employee()
Patu.language = "Java" # This is an instance attribute
Patu.getinfo()
Patu.greet()
print(Patu.language, Patu.salary)