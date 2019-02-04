from utils import libgen
import json
import time

def download_data(search='Python'):
    value_list = libgen.main(search)
    with open('data/data.json', 'w') as fp:
        json.dump(value_list, fp)
# print("done")
# value_list = libgen.main("Python")
# with open('data.json', 'w') as fp:
#     json.dump(value_list, fp)
# time.sleep(3)
def get_data():
    with open('data/data.json', 'r') as fp:
        data = json.load(fp)
    value_list = data
    return value_list