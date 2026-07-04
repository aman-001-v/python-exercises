subject_0 = {'first_name': 'tsiring', 
             'last_name':'youdon' , 
             'age': 22 , 
             'city':'ladakh',
             }
print(subject_0['first_name'])
print(subject_0['last_name'])
print(subject_0['city'])
print(subject_0['age'])

subject_1 = {'first_name': 'Harsh', 
             'last_name':'verma' , 
             'age': 20, 
             'city':'delhi',
             }
subject_2 = {'first_name': 'shivangi', 
             'last_name':'verma' , 
             'age': 21 , 
             'city':'west bengal',
             }
people = [subject_0 , subject_1 , subject_2]

for d in people:
    for k , v in d.items():
        print(f"{k} : {v}")