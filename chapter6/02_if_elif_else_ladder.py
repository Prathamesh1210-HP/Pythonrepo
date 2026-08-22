a = int(input("Enter your age: "))
# if elif else ladder
if(a==0) or (a<0):
    print("Invalid number of age. Please enter right age")
elif(a>=18):
    print("You are above the age of consent.")

else:
    print("You are below the age of consent.")

print("Execution done...")