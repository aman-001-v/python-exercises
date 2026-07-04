#usernames = ["harsh", "aman" , "uday" , "admin" , "mayank" , "ayush"]
usernames = []
if usernames:
    for user in usernames:
        if user == "admin":
            print("hello admin, please touch me.")
        else:
            print(f"hello {user}, thanks for login again.")

else:
    print("we need to find some users.")