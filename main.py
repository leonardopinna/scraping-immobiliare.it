import pandas as pd
from bs4 import BeautifulSoup
import urllib.request
import parameters as params
import time
import random

# FUNCTIONS DEFINITION

# Creates a BeautifulSoup HTML object from an url
def get_HTML_soup_object(url: str) -> BeautifulSoup:
    # Get the html of the website and convert it into text
    web_url = urllib.request.urlopen(url)
    data = web_url.read()

    # Create the soup object with the html
    soup = BeautifulSoup(data, 'html.parser')
    return soup


# Creates the query parameteres section of the url
def createFilterList(filter_object: dict) -> str:
    string = ""

    for f in filter_object:
        string += f"{f}={filter_object[f]}&"

    return string


# Creates the complete link with query parameteres
def create_link(base: str, type: str, location: str, filters: dict) -> str:
    return (base + "/" + type + "/" + location + "/?" + createFilterList(filters))[:-1]


# START OF THE SCRAPING

filters = dict()

# Add the base query search (customizable)
filters["criterio"] = "prezzo"
filters["ordine"] = "asc"

# Create the link to be scraped
location = input("Scegli la città dove vuoi cercare le case disponibili.\n").lower().replace(" ", "-")

# Serie di domande che possono essere inserite in una interfaccia
filters["prezzoMinimo"] = input(
    "Scegli il prezzo minimo dell'immobile (Vuoto: no prezzo minimo)\n")
filters["prezzoMassimo"] = input(
    "Scegli il prezzo massimo dell'immobile (Vuoto: no prezzo massimo)\n")

link = create_link(params.base_link, params.type["vendita"], location, filters)

# Get the html content of the page
main_soup = get_HTML_soup_object(link)

# Get the max number of pages for the research
try:
    max_page = main_soup.find_all(
        "div", class_="in-pagination__item")[-1].get_text()
except:
    max_page = 1


# Get the content of the announces
links = []
titles = []
prices = []

# For every page, scrape the desired contents
for i in range(0, int(max_page)):

    # Add the page query to the link
    filters["pag"] = i
    page_link = create_link(
        params.base_link, params.type["vendita"], location, filters)

    # Get the page content
    soup = get_HTML_soup_object(page_link)

    # Find all the announces for the current page
    collection = soup.find_all("li", class_="nd-list__item")

    # For every found real estate, get the title, price and link and put them in an array
    for item in collection:
        box = item.find("a", class_="in-card__title")
        price = item.find("li", class_="in-feat__item--main")

        if box != None:
            links.append(box["href"])
            titles.append(box["title"])
            prices.append(price.get_text())

    time.sleep(random.randint(1, 500)/1000)


# Create the dataframe of the found data
df = pd.DataFrame({'Title': titles, 'Prices': prices, "Link": links})

# Convert the dataframe in csv file
df.to_csv('./data.csv', index=False)

print(f"I found {str(len(links))} results. You can see them in the data.csv file.\n\
      If you want to see the actual results, you can go here:\n{link}")
