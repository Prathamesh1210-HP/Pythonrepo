class Employee:
    language = "Py" # This is a class attribute
    salary = 1400000

Patu = Employee()
Patu.name = "Patu" # This is an instance attribute
print(Patu.name ,Patu.language, Patu.salary)

rohan = Employee()
rohan.name = "Rohan" # This is an instance attribute
print(rohan.name, rohan.salary, rohan.language)

'''
Here name is an attribute and salary  and language are class attributes as they directly belong to the class
'''