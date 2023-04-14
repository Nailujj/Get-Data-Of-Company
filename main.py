import requests
from bs4 import BeautifulSoup
from getDataForCompany import get_company_website
import csv



found_elements = []

def getAllCompanies():
    # URL der HTML-Seite
    url = 'https://www.spectaris.de/medizintechnik/mitglieder/'
    counter = 0
    # HTML-Seite herunterladen und parsen
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Alle <h3>-Elemente in der Seite finden
    h3_elements = soup.find_all('h3')

    # Titel der HTML-Elemente suchen, die innerhalb eines <h3>-Elements gefunden werden
    for h3 in h3_elements:
        # Alle HTML-Elemente innerhalb des aktuellen <h3>-Elements finden
        elements = h3.find_all()
        
        # Titel jedes HTML-Elements ausgeben
        for element in elements:
            title = element.get('title')
            if title:
                element_dict = {
                    'index': counter,
                    'name': title
                }
                found_elements.append(element_dict)
        counter += 1

getAllCompanies()



for element in found_elements:
   element["website"] = get_company_website(element["name"])

   with open("companies.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=element.keys())
    writer.writeheader()

    for el in found_elements:
       writer.writerow(el)




