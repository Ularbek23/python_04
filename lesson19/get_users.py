import requests

server_response = requests.get("https://jsonplaceholder.typicode.com/users")
print(server_response.status_code)

data = server_response.json()
# print(data)
print(type(data))
names = []
for element in data:
    names.append(element["name"])

print(names)

with open("users.txt", "w") as users_file:
    for name in names:
        users_file.write(f"{name}\n")

