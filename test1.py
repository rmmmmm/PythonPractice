
import requests
import json
from bs4 import BeautifulSoup
# url='https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=recommend&page_limit=20&page_start=60'
l='https://movie.douban.com/subject/1292720/?tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&from=gaia_video'
response= requests.get(l)
# response.encoding='utf-8'
print(response.encoding)
# r= json.loads(response.text)
# movies=r['subjects'][0]['url']
# r2=requests.get(movies)
# print(r2.apparent_encoding)
# soup=BeautifulSoup(response.text,'lxml')
# # # print(soup.prettify())
# title=soup.find('span',attrs={'property':'v:summary'}).text
# print(title)

# print(movies)

# for m in movies:
    # movie = {}
    # movie['title'] = m['title']
    # movie['rate'] = str(m['rate'])
    # movie['url'] = m['url']
    # movielist.append(movie)
# print(movies)
