import os
import requests
from bs4 import BeautifulSoup
from datetime import date
import pandas as pd
import random
from dotenv import load_dotenv

load_dotenv()
FIXER_IO_API_KEY = os.getenv('FIXER_IO_API_KEY ')

def marathiNews():
    #specify the url of marathi news website
    url = "http://lokmat.com/"
    soup = get_source_code(url)
    news = soup.find('ul', class_='live-news-list')

    for i in news.findAll('li'):
        data = i.text
        return data

def tarikh():
    #specify the url of marathi date website
    url = "http://lokmat.com/"
    soup = get_source_code(url)
    tdate = soup.find('p', class_='today-date')
    return tdate.text

def suvichar():
    num = random.randrange(1,365)
    df = pd.read_csv("suvichar.csv", "r")
    data = df.iloc[num,0]
    return data

def graffiti():
    num = random.randrange(1,365)
    df = pd.read_csv("graffiti.csv", "r")
    data = df.iloc[num,0]
    return data

def dinVishesh():
    d = date.today().strftime('%d-%B').lstrip("0").replace(" 0", " ").lower()
    #specify the url of dinvishesh website
    url = f"http://www.dinvishesh.com/{d}-janm/" #जन्म तारखे नुसार
    soup = get_source_code(url)
    vishesh_content = soup.find('div', class_='col-md-8 mt-5')
    vishesh = vishesh_content.find_all('p')
    for data in vishesh:
        yield data.text

def bazar():
    url = "http://marathi.webdunia.com/"
    soup = get_source_code(url)
    business = soup.find('div', class_='business')
    for i in business.findAll('span'):
        data = i.text
        return data

def euro_to_inr():
    res = requests.get(f'http://data.fixer.io/api/latest?access_key={FIXER_IO_API_KEY}&symbols=USD,INR&format=1')
    result = res.json()
    inr = result['rates']['INR']
    usd = result['rates']['USD']
    usd_to_inr = inr/usd
    return usd_to_inr

def covid19():
    res = requests.get('https://api.covid19india.org/data.json')
    result = res.json()
    data = result['statewise']
    for stateinfo in data:
        if stateinfo['state'] == 'Maharashtra':
            return stateinfo

def get_source_code(url):
    page = requests.get(url)
    result = BeautifulSoup(page.text, 'html.parser')
    return result
