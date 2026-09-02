# It will print tables in mentioned numbers as well as it will create number of files as per tables.
def generateTable(n):
    table = ""
    for i in range(1,11):
          table += f"{n} X {i} ={n*i}\n"

    with open(f"tables/table_{n}.txt", "w") as f:
          f.write(table)


for i in range(2,21):
        generateTable(i)