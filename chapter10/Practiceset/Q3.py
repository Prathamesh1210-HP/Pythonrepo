# Create a class with a attribute a; create an object from it and set 'a' directly using object.a = 0. Does this change attribute?
class Demo:
    a = 0

o = Demo()
print(o.a)
o.a = 0
print(o.a)

# NO! class attributes never change
