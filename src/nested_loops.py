rows = int(input("Enter The No, of Rows: "))
columns = int(input("Enter the No, of columns: "))
symbol = input("Enter a Symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()