# Write a python program using function to convert Celsius to Farenheit.
# Formula: c/5 = (f-32)/9

# def f_to_c(f):
#     return 5*(f-32)/9    
    
# f = int(input("Enter the temperature in F: "))
# print(f"{f_to_c(f)} °C.")
    
def f_to_c(f):
    return 5*(f-32)/9

f = float(input("Enter the temperature in Farenheit: "))

print(f"Temperature after converting = {f_to_c(f)} °C")