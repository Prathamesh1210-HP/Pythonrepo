# A spam comment is defined as text containing following keywords:
# "make a lot of money","buy now",etc. Write a program to detect this all


c1 = "make a lot of money!"
c2 = "Whoaa! won a prize money!"
c3 = "Yeahhh! won a prize money!"
c4 = "Hello buddy! won a prize money!"

message = "make a lot of money! to but new things"
if(c1 in message or c2 in message or c3 in message or c4 in message):
    print("Its a fraud.")

else:
    print("Its legal")





































# c1 = "make a lot of money"
# c2 = "buy now"
# c3 = "subscribe this"
# c4 = "click this"

# message = input("Enter your message: ")

# if(c1 in message or c2 in message or c3 in message or c4 in message): # in check that string present in given string
#     print("It's a spam.")

# else:
#     print("It's not a spam.")