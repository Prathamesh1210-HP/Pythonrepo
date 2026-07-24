class Student:
    college_name = "ABC College";
    name= "Karan";
    print("Adding new student in Database..");

    # Parameterized constructors
    def __init__(self, name,marks):
        self.name = name;
        self.marks = marks;

    def welcome(self):
        print("Welcome student,",self.name)

s1 = Student("Arjun",98)
s1.welcome()
print(s1.name,s1.marks)
