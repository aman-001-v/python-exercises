current_users = ["haRsh", "aman" , "uday" , "admIn" , "mayank" , "ayuSh"]
new_users = ["john", "cena", "Harsh" , "nikhil" , "AYUSH"]
for i in range(len(current_users)):
    current_users[i] = current_users[i].lower()
if new_users:
    for i in new_users:
        if i.lower() in current_users:
            print(f"{i} is not available")
        else:
            print(f"{i} is available")
        