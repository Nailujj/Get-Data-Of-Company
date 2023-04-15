import requests
import re
from bs4 import BeautifulSoup
import os






def get_company_website(company_name):
    url = "https://www.google.com/search?q=" + company_name
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    search_results = response.text
    start = search_results.find('<cite')
    end = search_results.find('</cite>')
    website = search_results[start+7:end]
    return website.split(">")[1].split("<")[0]


def get_phone_and_mail(website):
    """
    Finds contact information on a website.
    Returns a dictionary with the following keys:
        - email: the email address listed on the website
        - phone: the phone number listed on the website
    If any information cannot be found, the corresponding value in the dictionary is None.
    """
    url = website
    url += '/impressum'

    try:

        response = requests.get(url, timeout=5, verify=False)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")

        # Find the email address
        email = None
        email_tags = soup.select("a[href^='mailto:']")
        if email_tags:
            email = email_tags[0]["href"][7:]

        # Find the phone number
        phone = None
        phone_tags = soup.find_all("a", href=True, text=True)
        for tag in phone_tags:
            if "tel:" in tag["href"]:
                phone = tag.text.strip()
                break
            elif "phone:" in tag["href"]:
                phone = tag.text.strip()
                break
            elif "Telefon:" in tag["href"]:
                phone = tag.text.strip()
                break
            elif "Telephone:" in tag["href"]:
                phone = tag.text.strip()
                break
            
        
        print(email)
        print(phone)
        # Return a dictionary with the contact information
        return {
            "email": email,
            "phone": phone,
        }

    except requests.exceptions.Timeout:
        pass


    url2 = website
    url2 += "/Kontakt"

    try:

        response = requests.get(url2, timeout=5, verify=False)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")

        # Find the email address
        email = None
        email_tags = soup.select("a[href^='mailto:']")
        if email_tags:
            email = email_tags[0]["href"][7:]

        # Find the phone number
        phone = None
        phone_tags = soup.find_all("a", href=True, text=True)
        for tag in phone_tags:
            if "tel:" in tag["href"]:
                phone = tag.text.strip()
                break
            elif "phone:" in tag["href"]:
                phone = tag.text.strip()
                break
            elif "Telefon:" in tag["href"]:
                phone = tag.text.strip()
                break
            elif "Telephone:" in tag["href"]:
                phone = tag.text.strip()
                break
            
        
        print(email)
        print(phone)
        # Return a dictionary with the contact information
        return {
            "email": email,
            "phone": phone,
        }

    except requests.exceptions.Timeout:
        pass



def get_only_mail(website):
    """
    Finds contact information on a website.
    Returns a dictionary with the following keys:
        - email: the email address listed on the website
        - phone: the phone number listed on the website
    If any information cannot be found, the corresponding value in the dictionary is None.
    """
    url = website
    url += '/impressum'

    try:

        response = requests.get(url, timeout=5, verify=False)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")

        # Find the email address
        email = None
        email_tags = soup.select("a[href^='mailto:']")
        if email_tags:
            email = email_tags[0]["href"][7:]
        
        print(email)
        
        # Return a dictionary with the contact information
        return  email
    

    except requests.exceptions.Timeout:
        pass


    url2 = website
    url2 += "/Kontakt"

    try:

        response = requests.get(url2, timeout=5, verify=False)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")

        # Find the email address
        email = None
        email_tags = soup.select("a[href^='mailto:']")
        if email_tags:
            email = email_tags[0]["href"][7:]
        
        print(email)

        # Return a dictionary with the contact information
        return email

    except requests.exceptions.Timeout:
        pass