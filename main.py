import requests
from bs4 import BeautifulSoup
import time

date = input("What year would you like to travel to? Type the date in this format YYYY-MM-DD: ")

time.sleep(2)
connection = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
connection_text = connection.text
print(connection.raise_for_status())

soup = BeautifulSoup(connection_text, "html.parser")

# first_title = soup.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
# all_titles = soup.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")
# print(all_titles)

names = soup.select("li ul li h3")
# print(names)

new_song_list = [text.getText().strip() for text in names]
print(new_song_list)
