import os
import requests
from urllib import request
from bs4 import BeautifulSoup

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
