import bs4 as bs
import sys
import urllib.request
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
        print('Connected to Libgen.')
        print('='*10)

    def Callable(self, html_str):
        self.html = html_str
        self.app.quit()

def main(url='http://libgen.pw/item/detail/id/801'):
    page = Page(url)
    soup = bs.BeautifulSoup(page.html, 'lxml')
    divs = soup.find('div', class_='book-info__download')
    table_rows = divs.find_all('a')
    d_link = []
    for i in table_rows:
        try:
            if i['href']:
                d_link.append(i['href'])
                # print (i['title'])
                # print (i['href'])
            else:
                continue
        except Exception:
            pass
    with open('data/downloadlink.json', 'w') as fp:
        json.dump(d_link, fp)
    print (d_link)
    # print (table_rows)

if __name__ == '__main__':
    main()
# with open('../data/mirrors.json', 'r') as fp:
#     data = json.load(fp)

# d_link = data['Libgen.pw']

# def get_download_link():
#     pass

# print(d_link)