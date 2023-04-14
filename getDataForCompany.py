import requests
import re
from bs4 import BeautifulSoup


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


