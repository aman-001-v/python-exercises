rivers = {'nile' : 'egypt' , 'indus': 'india' , 'ganga' : 'india', 'amazon':'south america'}
for r , c in rivers.items():
    print(f"The {r} runs through {c}")
for i in rivers.keys():
    print("River name: ", i)
for i in rivers.values():
    print("country name: ", i)