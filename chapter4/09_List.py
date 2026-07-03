friends = ["Apple","Orange",5,345.06,False, "Akash","Rohan"]

print(friends)
# print(friends[2])
friends[0] = "Grapes" # Unlike strings lists are mutable
print(friends[0])

print(friends[1:4])

# Methods of lists
friends.append("Patu")
print(friends)

l1 = [1,34,62,2,6,11]
l1.sort()
print(l1)
l1.reverse()
print(l1)

l1.insert(3, 333333) # Insert 333333 such that its index in the list is 3
print(l1)

print(l1.pop(3))  
print(l1)