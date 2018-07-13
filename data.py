import urllib.request
from bs4 import BeautifulSoup
from datetime import date

def marathiNews():
    #specify the url of marathi news website
    url = "http://www.lokmat.com/"

    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    news = soup.find('ul', class_='live-news-list')

    for i in news.findAll('li'):
        data = i.text
        return data

def suvichar():
    return ''

def dinVishesh():
    d = date.today().strftime('%d-%B').lstrip("0").replace(" 0", " ").lower()
    #specify the url of marathi news website
    url = "http://www.dinvishesh.com/{}-janm/".format(d) #जन्म तारखे नुसार 
    ghatana = "http://www.dinvishesh.com/{}-ghatana/".format(d) #घटने नुसार 
    mrutyu = "http://www.dinvishesh.com/{}-mrutyu/".format(d) #मृत्यू नुसार
   
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, 'html.parser')
    vishesh = soup.find('div', class_='td-post-content')
    data = vishesh.text[:260]
    return data
