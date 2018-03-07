# -*- coding: utf-8 -*-

# @author: chenjianlin
# @create: 2018-03-07 9:45
import logging

import requests


# r = requests.get('https://www.baidu.com/get')
# r.encoding ='utf-8'
# print(type(r))
# print(r.status_code)
# print(r.headers)

# print(type(r.text))
# with open('baidu.html', 'w+', encoding='utf-8') as f:
#     f.write(r.text)
# print(r.text)
# print(r.cookies)


# f1 = {'baidu': open('baidu.html', 'rb')}
# r = requests.post('http://httpbin.org/post', files=f1)
# print(r.text)


# r = requests.get('http://www.baidu.com')
# print(r.cookies.s)
#
# for key, value in r.cookies.items():
#     print(key + '=' + value)



# headers = {
#     'Cookie': '_zap=55ccd26c-0c1f-4874-a452-900e880005a2; q_c1=5fbe01dc06f144a4a69b1d3c551dde79|1519922171000|1519922171000; l_cap_id="YWJjOWMyZTY3YTkxNGQxYjk4ZGIyOWNlY2MzMTFmMDI=|1520216741|1e341fe9bfa6e390eb864ea12ffd699721ed96d2"; r_cap_id="M2Q1NWIzYTU4Y2UzNDQ5ZWE4NmIzMGIxZTBkNjQ3MTQ=|1520216741|db5608cd9d435c11cd9d0cba77eee69f146fe373"; cap_id="ZDA3OTRkNGJjY2Q4NGMwMjhiMDk2ZmU0ZjU4ZGU1OGY=|1520216741|6f79ce1a65722e429c244a34d4a760f54f4de783"; aliyungf_tc=AQAAAOrSqAiJhwIAOpTKb44OE9GT2N39; _xsrf=c45bb7c9-64e3-424e-b176-2768a23bba26; d_c0="ABDtXv5nPg2PTrIVR9l7uQDWbYhRE4SdSr8=|1520306310"; capsion_ticket="2|1:0|10:1520393297|14:capsion_ticket|44:ZWY5MzM2Y2UyMzVlNGYwYWFiODkyMjU4MzMzZGZhZGY=|988ecdf5bd5158ac476906e72470a2f6dbcc0897ced97895d269141f94adf20f"; z_c0="2|1:0|10:1520393301|4:z_c0|92:Mi4xXzdWOUFBQUFBQUFBRU8xZV9tYy1EU1lBQUFCZ0FsVk5WYXFNV3dBZnktam5FdXBNRy1Tcm5XV0YzbVd0ZlloeFB3|9b4c2771254c56a8e336aaa8411fa2dddf135815a7e68ca6d364bc01042d2480"',
#     'Host': 'www.zhihu.com',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
# }
#
# r = requests.get('https://www.zhihu.com', headers= headers)
# print(r.text)
# print(r.status_code)


# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/number/123456789')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)


logging.captureWarnings(True)
r = requests.get('https://www.12306.cn', verify=False)
print(r.status_code)