my_pizzas = ["dominos", "pizza hut" , "overstory", "99 cents"]
friend_pizzas = my_pizzas[:]
my_pizzas.append("pizza wings")
friend_pizzas.append("pizza galaria")
print("My favourate pizzas are:")
for i in my_pizzas:
    print(i)

print("My friend's favourate pizzas are:")
for i in friend_pizzas:
    print(i)