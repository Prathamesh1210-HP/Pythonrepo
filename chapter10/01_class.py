class Student:
    name= "Karan";
    print("Adding new student in Database..");

    # Default constructor
    def __init__(self):
        pass

    # Parameterized constructors
    def __init__(self, name,marks):
        self.name = name;
        self.marks = marks;

s1 = Student("Arjun",98)
print(s1.name,s1.marks)
s2=Student("Karna",90)
print(s1.name,s1.marks)