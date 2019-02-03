import bs4 as bs
import sys
import urllib.request
import requests
import json
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
import warnings
warnings.filterwarnings("ignore")

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

def main(url):
    # page = Page(url)
    page = requests.get(url)
    soup = bs.BeautifulSoup(page.text, 'html.parser')
    table = soup.find('table')
    table_rows = table.find_all('a')
    mirrors = {}
    for i in table_rows:
        try:
            if i['title']:
                mirrors[i['title']] = i['href']
                # print (i['title'])
                # print (i['href'])
            else:
                continue
        except Exception:
            pass
    with open('data/mirrors.json', 'w') as fp:
        json.dump(mirrors, fp)
    # print (mirrors)
    return (mirrors)

if __name__ == '__main__':
    main("http://gen.lib.rus.ec/book/index.php?md5=AEE7239FFCF7871E1D6687CED1215E22")