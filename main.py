import requests
from bs4 import BeautifulSoup
from getDataForCompany import get_company_website
import csv



found_elements = []

def getAllCompanies():
    # URL of the HTML-page
    url = 'https://www.spectaris.de/medizintechnik/mitglieder/'
    counter = 0
    # download HTML page and parse
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # get all h3 elements in page (i looked at it beforehand to know which element the company title would be)
    h3_elements = soup.find_all('h3')

    # Look for titles within h3
    for h3 in h3_elements:
        
        elements = h3.find_all()
        
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


#loop through found titles and get websites

for element in found_elements:
   element["website"] = get_company_website(element["name"])
    
    #create csv
   with open("companies.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=element.keys())
    writer.writeheader()

    for el in found_elements:
       writer.writerow(el)




