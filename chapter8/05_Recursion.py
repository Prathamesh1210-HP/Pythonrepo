# def facto(n):
#     if(n==1 or n==0):
#         return 1
#     return n * facto(n-1)

# n = int(input("Enter a number: "))
# print(f"The factorial of this number is: {facto(n)}")

def facto(n):
    if (n==1 or n==0):
        return 1;
    return n* facto(n-1);

n = int(input("Enter a number: "))
print(f"The factorial of this number is: {facto(n)}")