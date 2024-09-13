import requests
from bs4 import BeautifulSoup
import csv

# Define the URL of the website to scrape
url = "http://books.toscrape.com/"

# Send a GET request to the website
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the data you want to scrape
    books = soup.find_all('article', class_='product_pod')

    # Open or create a CSV file to store the data
    with open('books.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        # Write the header row
        writer.writerow(['Title', 'Price'])

        # Loop through the found elements and extract information
        for book in books:
            book_title = book.h3.a['title']
            book_price = book.find('p', class_='price_color').get_text()
            
            # Write book title and price to CSV file
            writer.writerow([book_title, book_price])

    print("Data saved to books.csv")
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
