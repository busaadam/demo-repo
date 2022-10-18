# basic authentication
import json

file = open("secrets.json", "r")
data = file.read()
file.close()



auth = json.loads(data)
print(type(auth))

username = input("Adja meg a felhasználó nevét: ")
password = input("Adja meg a jelszavát: ")

if  username == auth["username"] and password == auth ["password"]:
    print("Üdv a fedélzeten!")
else:
    print("Nincs engedélyezve a belépés!")
