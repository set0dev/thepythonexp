# Continue.
money = "568$23"

for i in money:
    if i == "$":
        continue
    print(i, end="")
