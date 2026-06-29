d = {} # This is how empty dictionary get created by user
marks = {
    "Prathamesh":100,
    "Patu":80,
    "Raju":70
}

# print(marks, type(marks))
# print(marks["Prathamesh"])
# print(marks)

# Methods
print(len(marks))
print(marks.items()) # Prints specific items
print(marks.keys()) # Prints specified keys "Patu":80 (Patu is key)
print(marks.values()) # Prints all assigned values "Patu": 80 (80 is value)
marks.update({"Prathamesh":99}) # Proof of mutability by updation
print(marks)
# print(marks.get("Patu2")) # prints none
# print(marks["Patu2"]) # returns ann error

# Properties 

# It is unordered.
# It is mutable.
# It is indexed.
# Cannot contain duplicate keys.