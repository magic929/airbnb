import requests
from bs4 import BeautifulSoup
import urllib.request
import sys

def get_html(url):
    try:
        req = requests.get(url=url)
        return req.text
    except Exception as e:
        print("error : ", e)


def get_links(html):
    bf = BeautifulSoup(html, 'lxml')
    table = bf.find('table', class_="table table-hover table-striped amsterdam").find('tbody')
    links = []
    for t in table.find_all('tr'):
        # print(t)
        links.append(t.find('a', href=True)['href'])
    return links

def download(links):
    try:
        for l in links:
            filename = l.split('/')[-4:]
            filename = "_".join(filename)
            urllib.request.urlretrieve(l, './data/'+filename)
        return 1
    except Exception as e:
        print("error: ", e)


if __name__ == "__main__":
    html = get_html(sys.argv[1])
    links = get_links(html)
    download(links)
    
        
    

