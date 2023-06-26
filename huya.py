import os
from urllib import request

import requests
from bs4 import BeautifulSoup

# from subprocess import call
# from importlib import metadata as importlib_metadata

if not os.path.exists('img'):
    os.mkdir('img')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 '
                  'Safari/537.36 Edg/112.0.1722.39'
}

url = 'https://www.huya.com/g/xingxiu'
response = requests.get(url, headers=headers).text
soup = BeautifulSoup(response, 'lxml')
girls = soup.find_all('img', class_='pic')
for girl in girls:
    girl_url = girl['data-original'].split('?')[0]
    girl_title = girl['title']
    try:
        request.urlretrieve(girl_url, f'img/{girl_title}.jpg')
        request.urlcleanup()
    except Exception as e:
        print(e)
        print('error:', girl_title)

# for dist in importlib_metadata.distributions():
#     print("Updating for:", dist.metadata["Name"])  # 看进度用，非必需
#     call("pip install -U " + dist.metadata["Name"], shell=True)
