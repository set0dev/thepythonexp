capitals = {
    'Haryana' : 'New Delhi',
    'Karnataka' : 'Bangalore',
    'Tamil Nadu' : 'Chennai',
    'Kerala' : 'Trivandrum',
}

#capitals.update
# removes something using the pop, keyword
#thank god I'm using an ide, or I can't code for real.

for key, value in capitals.items():
    print(key, value)

print(capitals.get("Germany"))
print(capitals.keys())
print(capitals.values())
print(capitals.items())