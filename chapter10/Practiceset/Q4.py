# Add a static method in problem 2, to greet the user with hello.

class Employee:
   
    @staticmethod # There's no need to get self as argument when it declared as @staticmethod 
    def greet():
        print("Hello")

Patu = Employee()
print(Patu.greet())