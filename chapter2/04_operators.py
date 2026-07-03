# Arithmetic Operators
a = 34
b = 4
c = a + b
print(c)

# Assignment Operators
a = 4-2 # Assign 4-2 in a
print(a)
# b = 6
b += 3 # Increment the value of b by 3 and then assign it to b
b -= 3 # Decrement the value of b by 3 and then assign it to b
print(b)

# Comparison Operator
d = 5==5
print(d) # It returns always boolean <=, >=, -=, +=, *=, /=, !=, ==
# A=5 means you are assigning value 5 to A.
# 5==5 means you are declaring the value of 5 is 5.

# Logical operators
# TT of 'or':
e = True or False # If one option is true it will define value true & both options get false it'll define as false
print("True or False is ",True or False)
print("True or True is ",True or True)
print("False or True is ",False or True)
print("False or False is ",False or False,"\n")

#TT of 'and':
# If one option is False it will define value False & both options are True it'll define as True
e = True and False
print("True and False is ",True and False)
print("True and True is ",True and True)
print("False and True is ",False and True)
print("False and False is ",False and False,"\n")

# The operator which makes True = False and False = True is Not operator
print(not(True))