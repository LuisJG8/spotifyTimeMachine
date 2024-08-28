import requests
from bs4 import BeautifulSoup


# year = input("What year would you like to travel to? Type the date in this format YYYY-MM-DD: ")

connection = requests.get(f"https://www.billboard.com/charts/hot-100//")
connection_text = connection.text
print(connection.raise_for_status())

soup = BeautifulSoup(connection_text, "html.parser")

all_titles = soup.find(name="li", class_="lrv-u-width-100p")
print(all_titles)

# 2001-08-12
















