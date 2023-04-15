import requests
from bs4 import BeautifulSoup
from getDataForCompany import get_company_website
from getDataForCompany import get_only_mail
import csv



found_elements = []


def getAllCompaniesFromWebsite():
    counter = 0

    # URL of the HTML-page
    url = 'https://www.spectaris.de/medizintechnik/mitglieder/'
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
getAllCompaniesFromWebsite()



def getCompaniesFromChatGPT():
    with open('list.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        counter = 146
        for row in reader:
            result = "".join(row)
            counter += 1
            element_dict = {
                        'index': counter,
                        'name': result
            }
            found_elements.append(element_dict)
getCompaniesFromChatGPT()
        



#loop through found titles and get websites
for element in found_elements:
    element["website"] = get_company_website(element["name"])
    element["contact"] = get_only_mail(element["website"])
    
   #create csv
    with open("companies.csv", "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=element.keys())
        writer.writeheader()

        for el in found_elements:
            writer.writerow(el)
    
    if element["index"] == len(found_elements):
       break




