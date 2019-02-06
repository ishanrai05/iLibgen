import json
import requests

from utils import getDownloadLink

from settings import DOWNLOAD_PATH


def main():
    with open('data/downloadlink.json', 'r') as fp:
            data = json.load(fp)
            
    ext = data['Extension']
    title = data['Title']
    file_name = str(title) + '.' + str(ext)
    url = data['Libgen.pw']
    file_url = getDownloadLink.main(url)

    # file_url = "http://codex.cs.yale.edu/avi/db-book/db4/slide-dir/ch1-2.pdf"
    
    r = requests.get(file_url, stream = True) 
    
    with open(DOWNLOAD_PATH+file_name,"wb") as f: 
        for chunk in r.iter_content(chunk_size=1024): 
    
            # writing one chunk at a time to pdf file 
            if chunk: 
                f.write(chunk) 
    # print(data)

if __name__ == '__main__':
    main()