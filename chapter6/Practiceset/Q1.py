# Write a program to find out the greatest of four numbers entered by the user

n1,n2,n3,n4 = 80,20,30,40;

if(n1>n2 and n1>n3 and n1>n4):
    print(f"{n1} is greater.")
elif(n2>n1 and n2>n3 and n1>n4):
    print(f"{n2} is greater.")
elif(n3>n2 and n3>n2 and n3>n4):
    print(f"{n3} is greater.")
elif(n4>n2 and n4>n3 and n4>n1):
    print(f"{n4} is greater.")
else:
    print("Invalid number.")
