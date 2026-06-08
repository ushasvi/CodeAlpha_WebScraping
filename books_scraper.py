import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

books = []

for book in soup.find_all("article", class_="product_pod"):
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    rating = book.p["class"][1]

    books.append([title, price, rating])

df = pd.DataFrame(books, columns=["Title", "Price", "Rating"])

df.to_csv("books_data.csv", index=False)

print(df.head())
print("Data saved successfully!")
