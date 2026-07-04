animals = ["cat" , "dog" , "cow" , "goat" , "sheep"]
for animal in animals:
    print(f"{animal} is a great pet")

print("They all are mammels.\n")

print(f"First three items in the list are: {animals[:3]}")
print(f"Three items in the middle are: {animals[int((len(animals)/2)-1):int((len(animals)/2)+2)]}")
print(f"Three animals from the end are: {animals[-3:]}")