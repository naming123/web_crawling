import requests
from bs4 import BeautifulSoup as bs

url = 'https://ee.korea.ac.kr/community/undernotice.html?schType=subject&schText=%EC%9E%A5%ED%95%99%EA%B8%88'
response = requests.get(url)
response.encoding = 'utf-8'
print(response.text)