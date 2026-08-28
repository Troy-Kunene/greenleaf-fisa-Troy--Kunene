import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1")
data = response.json()

print("Supplier name:", data["name"])
print("Supplier email:", data["email"])
