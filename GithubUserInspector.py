import requests
import json
import time

def timer(original_func):
   def wrapper(*args , **kwargs):
      t = time.time()
      result = original_func(*args , **kwargs)
      t1 = time.time()
      print("Runtime: {} seconds".format(t1-t))
      return result;
   return wrapper

@timer
def fetch_user(username):
    try:
        r = requests.get("https://api.github.com/users/{}".format(username) , timeout = 2)
        r.raise_for_status()
        data = r.json()
        file_data = {"Name" : data["name"] ,
                    "Username" : data["login"] ,
                    "Bio" : data["bio"] ,
                    "Location" : data["location"] ,
                    "Public Repositories" : data["public_repos"] ,
                    "Followers" : data["followers"] ,
                    "Following" : data["following"] ,
                    "Created At" : data["created_at"]
                    }
        
        for i in file_data:
           if file_data[i] is None:
              file_data[i] = "Not Available"

        return file_data
    
    except requests.exceptions.Timeout:
        print("Request timed out")
    except requests.exceptions.ConnectionError:
        print("Connection failed")
    except requests.exceptions.HTTPError:
        print("Bad HTTP status")
    except requests.exceptions.RequestException as e:
        print(f"Other request error: {e}")

user_data = dict()
while True:
   username = input("Enter GitHub Username: ")
   file_data = fetch_user(username)
   user_data[username] = file_data
   n = input("Wanna search more(y/n): ")
   if n == 'n':
    break     

with open("github_userdata.json",'w') as f:
    json.dump(user_data , f , indent = 2)

