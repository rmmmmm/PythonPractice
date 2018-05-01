# 爬虫 豆瓣电影评分
import requests
from bs4 import BeautifulSoup
import json
import time
def get_html(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding='utf-8'
        time.sleep(0.5)
        return r.text
    except:
        return 'something error'

def get_movieurl(url):
    contents=json.loads(get_html(url))
    movies=contents['subjects']
    urllist=[]
    for m in movies:
        detailurl=m['url']
        urllist.append(detailurl)

    return urllist

def get_moviedetail(url):
    urllist=get_movieurl(url)
    contents = []
    for l in urllist:
        movie={}
        html=get_html(l)
        soup=BeautifulSoup(html,'lxml')
        try:
            movie['title']=soup.find('span',attrs={'property':'v:itemreviewed'}).text
            movie['year']=soup.find('span',attrs={'class':'year'}).text
            movie['rate']=soup.find('strong',attrs={'class':'ll rating_num'}).text
            movie['description']=soup.find('span',attrs={'property':'v:summary'}).text.replace(' ','')
            # print(movie['title'])
            contents.append(movie)
        except:
            print('error')
    return contents


def SaveToFile(dict):

    with open('DoubanMovies.txt','a+',encoding='utf-8') as f:
        for m in dict:
            f.write('名称：{} \t 年份：{} \t 评分：{} \t \n简介：\t{}\t\n\n'.format(m['title'],m['year'],m['rate'],m['description']))
    print('写入完成')

def main(base_url):
    pages=0
    url=base_url+'&page_start='+str(pages*20)
    movies=get_moviedetail(url)
    while len(movies):
        url = base_url + '&page_start=' + str(pages * 20)
        movies = get_moviedetail(url)
        print(len(movies))
        SaveToFile(movies)
        pages = pages + 1
        print(pages)
        print('第{}页已爬完'.format(pages))

base_url='https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=recommend&page_limit=20'


if __name__ == '__main__':
    main(base_url)


