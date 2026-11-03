# PA1107 - Web scrapping
# Fetching website content using requests and BeautifulSoup

import requests
from bs4 import BeautifulSoup
import csv

url = "https://quotes.toscrape.com/"
response = requests.get(url)


# Display status code
print(f"Status Code: {response.status_code}")

soup = BeautifulSoup(response.text, "html.parser")

# extracting website heading 
heading = soup.find("h1").text
print(f"Website Heading: {heading}")

span = soup.find("span")
print(f"Span Text: {span.text}")

small = soup.find("small")
print(f"Small Text: {small.text}")

#find all
quotes = soup.find_all("div", class_= "quote")

qoute_data = []

for quote in quotes:
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text

    # Display the extracted data
    print(f"Quote: {text}")
    print(f"Author: {author}")

# save data to csv file
with open("quotes.csv", "w", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Quote", "Author"])
    for quote in quotes:
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        writer.writerow([text, author])