# -*- coding: utf-8 -*-

# @author: chenjianlin
# @create: 2018-03-08 0:00
from urllib.parse import urlencode

from pyquery import PyQuery as pq
import requests

base_url = 'https://m.weibo.cn/api/container/getIndex?'

headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2830678474',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}


def get_page(page):
    params = {
        'type': 'uid',
        'value': '2830678474',
        'containerid': '1076032830678474',
        'page': page
    }

    url = base_url + urlencode(params)

    try:
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            return r.json()
    except requests.ConnectionError as e:
        print('Error', e.args)


def parse_page(j):
    if j:
        items = j.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            weibo = {}
            weibo['id'] = item.get('id')
            weibo['text'] = pq(item.get('text')).text()
            weibo['attitudes'] = item.get('attitudes_count')
            weibo['contents'] = item.get('comments_count')
            weibo['reposts'] = item.get('reposts_count')
            yield weibo


for page in range(1, 11):
    json = get_page(page)
    # print(json)
    r = parse_page(json)
    for i in r:
        print(i)
