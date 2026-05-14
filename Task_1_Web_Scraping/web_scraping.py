import requests
from bs4 import BeautifulSoup
import pandas as pd

# Empty lists
quotes = []
authors = []
tags_list = []

# Loop through multiple pages
for page in range(1, 6):

    url = f"https://quotes.toscrape.com/page/{page}/"

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    quote_data = soup.find_all("div", class_="quote")

    for item in quote_data:

        # Extract quote
        quote = item.find("span", class_="text").text

        # Extract author
        author = item.find("small", class_="author").text

        # Extract tags
        tags = item.find_all("a", class_="tag")
        tag_text = ", ".join([tag.text for tag in tags])

        # Store data
        quotes.append(quote)
        authors.append(author)
        tags_list.append(tag_text)

# Create dataframe
data = pd.DataFrame({
    "Quote": quotes,
    "Author": authors,
    "Tags": tags_list
})

# Save CSV
data.to_csv("advanced_quotes_data.csv", index=False)

print("Advanced web scraping completed successfully!")