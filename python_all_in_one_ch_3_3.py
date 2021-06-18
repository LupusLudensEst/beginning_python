# Get request module from url library.
from urllib import request
# This one has handy tools for scraping a web page.
from bs4 import BeautifulSoup
# If you want to dump data to json file.
import json
# If you want to save to CSV.
import csv

# Sample page for practice.
page_url = 'https://alansimpson.me/python/scrape_sample.html'

# Open that page.
rawpage = request.urlopen(page_url)

# Make a BeautifulSoup object from the html page.
soup = BeautifulSoup(rawpage, "html.parser")

# Isolate the main content block.
content = soup.article

# Create an empty list for dictionary items.
links_list = []
# Loop through all the links in the article.
for link in content.find_all('a'):
    url = link.get('href')
    img = link.img.get('src')
    text = link.span.text
    links_list.append({'url': url, 'img': img, 'text': text})
    # Try to get the href, image url, and text.
    try:
        url = link.get('href')
        img = link.img.get('src')
        text = link.span.text
        links_list.append({'url': url, 'img': img, 'text': text})
        # If the row is missing anything...
    except AttributeError:
        # ... skip it, don't blow up.
        pass

# Save as a JSON file.
with open('links.json', 'w', encoding='utf-8') as links_file:
    json.dump(links_list, links_file, ensure_ascii=False)

# Save it to a CSV.
with open('links.csv', 'w', newline='') as csv_out:
    csv_writer = csv.writer(csv_out)
    # Create the header row
    csv_writer.writerow(['url', 'img', 'text'])
    for row in links_list:
        csv_writer.writerow([str(row['url']), str(row['img']), str(row['text'])])