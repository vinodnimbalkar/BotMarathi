import urllib.request, requests
from bs4 import BeautifulSoup
from datetime import date
import pandas as pd
import random

def marathiNews():
    #specify the url of marathi news website
    url = "http://www.lokmat.com/"

    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    news = soup.find('ul', class_='live-news-list')

    for i in news.findAll('li'):
        data = i.text
        return data

def tarikh():
    #specify the url of marathi date website
    url = "http://www.lokmat.com/"

    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
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
    url = "http://www.dinvishesh.com/{}-janm/".format(d) #जन्म तारखे नुसार 
    ghatana = "http://www.dinvishesh.com/{}-ghatana/".format(d) #घटने नुसार 
    mrutyu = "http://www.dinvishesh.com/{}-mrutyu/".format(d) #मृत्यू नुसार
   
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    vishesh = soup.find('div', class_='td-post-content')
    data = vishesh.text[:260]
    return data

def bazar():
    url = "http://marathi.webdunia.com/"
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    business = soup.find('div', class_='business')
    for i in business.findAll('span'):
        data = i.text
        return data

def bitcoin():
    res = requests.get('https://www.zebapi.com/api/v1/market/ticker/btc/inr')
    bitdata = res.json()
    buy_data = "खरेदी किंमत : "+ bitdata['buy']+"₹\n"
    sell_data = "विक्री किंमत : "+ bitdata['sell']+"₹"
    data = buy_data+sell_data
    return data