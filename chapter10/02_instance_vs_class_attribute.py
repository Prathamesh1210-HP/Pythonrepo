class Employee:
    language = "Py" # This is a class attribute
    salary = 1400000

Patu = Employee()
Patu.language = "Java" # This is an instance attribute
print(Patu.language, Patu.salary)