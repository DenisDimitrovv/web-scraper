from bs4 import BeautifulSoup
import requests
import csv

page_to_scrape = requests.get("https://www.imoti.net/bg/obiavi/r/prodava/burgas/?sid=gBkI5L")
soup = BeautifulSoup(page_to_scrape.text, 'html.parser')


offer_types = soup.findAll("span", attrs={"class":"re-offer-type"})
locations = soup.findAll("span", attrs={"class":"location"})
prices = soup.findAll("strong", attrs={"class":"price"})
parameters = soup.findAll("ul", attrs={"class":"parameters"})


data = list(zip(
    [offer_type.text for offer_type in offer_types],
    [location.text for location in locations],
    [price.text for price in prices],
    [parameter.text for parameter in parameters]
))

with open("imotinet.csv", "w", newline='') as file:
    writer = csv.writer(file)

    # Write the transposed data to CSV
    writer.writerow(["Offer Types", "Locations", "Prices", "Parameters"])
    for row in data:
        writer.writerow(row)

print("CSV file created successfully.")