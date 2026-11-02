# PA1102

import requests

# define api endpoint (combination of domain and path)
url = "https://jsonplaceholder.typicode.com/posts"

params = {
    "userId": 1
}

# send GET request with parameters to the API endpoint
response = requests.get(url, params=params)

print("Status code ", response.status_code)
print("URL requested: ", response.url)

data = response.json()

for post in data:
    print("Post ID", post["id"])
    print("Post Title", post["title"])
    print("------------------------------")