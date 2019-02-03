# search = "tensorflow"
# search = search.strip().replace(' ','+')
# url = f"http://libgen.io/search.php?req={search}"

import bs4 as bs
import sys
import urllib.request
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
import warnings
warnings.filterwarnings("ignore")

from utils import getMirrors


class Page(QWebEnginePage):
    def __init__(self, url):
        # Startup the webpage
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = ''
        self.loadFinished.connect(self._on_load_finished)
        # Connecting the methd
        self.load(QUrl(url))
        self.app.exec_()

    def _on_load_finished(self):
        self.html = self.toHtml(self.Callable)
        # print('Connected to Libgen.')
        # print('='*10)

    def Callable(self, html_str):
        self.html = html_str
        self.app.quit()


class StoreData(object):
    def __init__(self):
        self.book_data = {
                'SN' : '',
                'ID': '',
                'Author': '',
                'Title': '',
                'Publisher': '',
                'Year': '',
                'Pages': '',
                'Language': '',
                'Size': '',
                'Libgen Link': '',
                'Mirrors': '',
                'Extension': '',
            }
        self.data = []

    def insert_data(self,row,sn):
        self.book_data['SN'] = row[10]
        self.book_data['ID'] = row[0]
        self.book_data['Author'] = row[1]
        self.book_data['Title'] = row[2]
        self.book_data['Publisher'] = row[3]
        self.book_data['Year'] = row[4]
        self.book_data['Pages'] = row[5]
        self.book_data['Language'] = row[6]
        self.book_data['Size'] = row[7]
        self.book_data['Libgen Link'] = row [9]
        # self.book_data['Mirrors'] = row[11]
        for i in row[11]:
            self.book_data[i] = row[11][i]
        self.book_data['Extension'] = row[8]
        self.data.append(self.book_data.copy())

    def get_data(self):
        return(self.data)
    
    
def main(search = "Python"):
    search = search.strip().replace(' ','+')
    url = f"http://gen.lib.rus.ec/search.php?req={search}&res=25"
    # url = "http://gen.lib.rus.ec/search.php?req=python&res=25"
    page = Page(url)
    soup = bs.BeautifulSoup(page.html, 'lxml')
    table = soup.find('table', class_='c')
    # print(table)
    table_rows = table.find_all('tr')
    # print(table_rows)
    store_data = StoreData()
    sn=0
    for tr in table_rows:
        td = tr.find_all('td')
        # print(tr)
        # print(td)
        link = "http://gen.lib.rus.ec/"+[i['href'] for i in td[2].find_all('a')][-1]
        if sn == 0:
            sn += 1
            continue
        mirrors = getMirrors.main(link)
        # print (mirrors)
        row = [i.text for i in td]
        row[9] = link
        row[10] = sn
        row[11] = mirrors
        store_data.insert_data(row,sn)
        sn += 1

    ret = store_data.get_data()
    # print(ret)
    return (ret)
    
if __name__ == '__main__': 
    main("Java")