# PA1101 - Access the web and fetch internet data.

# Import requests library
import requests

# define api endpoint (combination of domain and path)
url = "https://jsonplaceholder.typicode.com/users"

# send GET request to the API endpoint
response = requests.get(url)

print("Status code ", response.status_code)

data = response.json()

#Display the data fetched from the API
print(data)


for user in data:
    print(user["name"])