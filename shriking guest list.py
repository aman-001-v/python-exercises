guest_list = ["kartik" , 'utkarsh' , 'kanishak' , 'nikhil' , 'mahima']
print(f"{guest_list[0].title()} miss you man.")
print(f"{guest_list[1].title()} miss you man.")
print(f"{guest_list[2].title()} miss you man.")
print(f"{guest_list[4].title()} you are fun")
print("\n")
print(f"{guest_list[2].title()} can't make it")
del guest_list[2]
guest_list.insert(2, "Kushal")
print("\n")
print(f"{guest_list[0].title()} miss you man.")
print(f"{guest_list[1].title()} miss you man.")
print(f"{guest_list[2].title()} miss you man.")
print(f"{guest_list[4].title()} you are fun")

print('\nFound a bigger table\n')
guest_list.insert(0 , "harsh")
guest_list.insert(0 , "Aman")
guest_list.append("anubis")

print(f"{guest_list[0].title()} miss you man.")
print(f"{guest_list[1].title()} miss you man.")
print(f"{guest_list[2].title()} miss you man.")
print(f"{guest_list[3].title()} miss you man.")
print(f"{guest_list[4].title()} you are fun")
print(f"{guest_list[5].title()} miss you man.")
print(f"{guest_list[6].title()} miss you man.")


print("Can only invite two of you")

print(f"{guest_list.pop(2)} sorry man")
print(f"{guest_list.pop(2)} sorry man")
print(f"{guest_list.pop(2)} sorry man")
print(f"{guest_list.pop(2)} sorry man")
print(f"{guest_list.pop(2)} sorry man")
print(f"{guest_list.pop(2)} sorry man")

print(f"{guest_list[0].title()} you are still invited")
print(f"{guest_list[1].title()} you are still invited\n")

del guest_list[0]
del guest_list[0]

print(guest_list)