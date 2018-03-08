# -*- coding: utf-8 -*-

# @author: chenjianlin
# @create: 2018-03-08 8:44
from _md5 import md5
from multiprocessing.pool import Pool
from urllib.parse import urlencode

import os
import requests


def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword':' 街拍',
        'autoload': 'true',
        'count': '20',
        'cur_tab': '1',
        'from': 'search_tab'
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print("Error: " + e.args)
        return None


def get_image(json):
    if json.get('data'):
        for item in json.get('data'):
            title = item.get('title')
            images = item.get('image_detail')
            if images:
                for image in images:
                    yield {
                        'image': image.get('url'),
                        'title': title
                    }


basePath = 'e:\\jiepai\\'


def save_image(item):
    path = basePath + item.get('title')
    if not os.path.exists(path):
        os.makedirs(path)
    try:
        response = requests.get(item.get('image'))
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')
            file_path = basePath + file_path
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(response.content)
            else:
                print('Already Download ', file_path)
    except requests.ConnectionError as e:
        print('Error: ' + e.args)


def main(offset):
    json = get_page(offset)
    for item in get_image(json):
        print(item)
        save_image(item)


GROUP_START = 1
GROUP_END = 10

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()

