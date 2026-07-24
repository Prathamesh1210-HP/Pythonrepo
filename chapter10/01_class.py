# Create student class that takes name and marks of 3 subjects as arguments in constructor. Then create a method to print the average.

class Student:
    print("...Student's result...");

    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    @staticmethod
    def hello():
        print("Hello")   

    def getavg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("Hi", self.name, "Your avg score is: ", sum/3 )

s1 = Student("Tony stark", [99,98,97])
s1.getavg()
s1.hello()
# print(s1.name,m1,m2,m3)