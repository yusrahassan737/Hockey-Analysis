# Title: Web Scraping Python Script
# Name: Yusra Hassan
# Last Updated: March 12th, 2025
# Description: Script to scrape some hockey teams data

from bs4 import BeautifulSoup
import requests
import pandas as pd

page = requests.get("https://www.scrapethissite.com/pages/forms/?page_num=1&per_page=600") # used a shortcut to get all data on one page
soup = BeautifulSoup(page.text, "html.parser")
table = soup.table

# Extract headers
heads = table.find_all("th")
heads_tidy = []
for i in heads:
    heads_tidy.append(i.string.strip()) # get just the data part

# Extract rows
data = []
rows = table.find_all_next("tr", {"class": "team"}) # reason for next: ignore the headings
for i in range(len(rows)):
    temp_row = rows[i].find_all("td")
    tidy_row = []
    for j in temp_row:
        tidy_row.append(j.string.strip())
    data.append(tidy_row)

df = pd.DataFrame(data, columns = heads_tidy)
df.to_csv("team_wins_losses.csv")