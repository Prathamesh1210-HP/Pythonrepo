word = "Donkey"

with open("donke.txt", "r")as f:
    content  = f.read()

contentNew = content.replace("Donkey", "#####")

with open("donke.txt", "w") as f:
    f.write(contentNew)

print("Done.")