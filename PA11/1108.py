import requests

url = "https://mlabassessmentcenter.web.app"

response = requests.get(url, verify=True, timeout=100)

print(f"Website: {url}")
print(f"Status Code: {response.status_code}")
print(f"Final URL: {response.url}")

if response.url.startswith("https://"):
    print("Website uses HTTPS")
    print("Connection successful!")
else:
    print("Website does not use HTTPS")