import bs4 as bs
import sys
import urllib.request
import requests

def main(url):
    page = requests.get(url)
    soup = bs.BeautifulSoup(page.text, 'html.parser')
    # print(soup)
    link = (soup.find('div', class_='book-info__download')).find('a')['href']
    return(link)

if __name__ == '__main__':
    main('http://booksdescr.com/item/detail/id/1482')