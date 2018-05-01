# -*- coding: utf-8 -*-
import requests
import time
from bs4 import BeautifulSoup



# 抓取网页

def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        # 如果状态码不是200，则引发HTTPERRPR异常
        r.raise_for_status()
        r.encoding = 'utf-8'
        # print(r.text)
        return r.text
    except:
        return 'Error'

# 分析网页文件，整理信息，保存在列表中
def get_content(url):

    comments=[]
    html=get_html(url)

    soup=BeautifulSoup(html,'lxml')

    liTags=soup.find_all('li',attrs={'class':' j_thread_list clearfix'})

    for li in liTags:
        comment={}

        # 加一个try except 防止爬虫找不到信息停止运行
        try:
            comment['title']=li.find('a',attrs={'class':'j_th_tit '}).text
            comment['link']='http://tieba.baidu.com/'+li.find('a',attrs={'class':'j_th_tit '})['href']
            # strip()去掉句首句尾字符，默认为空格
            comment['name']=li.find('span',attrs={'class':'tb_icon_author '}).text.strip()
            comment['time'] = li.find(
                'span', attrs={'class': 'pull-right is_show_create_time'}).text.strip()
            comment['replyNum'] = li.find(
                'span', attrs={'class': 'threadlist_rep_num center_text'}).text.strip()

            comments.append(comment)
        except:
            print('ops!something happend!')

    return comments

# 将爬到的文件写入到本地，保存到Bigbang.txt文件中
def SaveToFile(dict):

    with open('Bigbang.txt','a+',encoding='utf-8') as f:
        for comment in dict:
            f.write('标题： {}\t 链接：{}\t 发帖人：{}\t 发帖时间：{}\t 回复数量：{}\n'.format(
                comment['title'], comment['link'], comment['name'], comment['time'], comment['replyNum']
            ))

        print('当前页面爬取完成')


def main(base_url,deep):
    url_list=[]
    #把所有要爬取的url存入列表
    for i in range(0,deep):
        url_list.append(base_url+'&pn='+str(50*i))
    print('所有网页已经下载到本地！开始筛选信息。。。')

    for url in url_list:
        content=get_content(url)
        SaveToFile(content)
    print('所有信息都保存完毕！')

base_url = 'http://tieba.baidu.com/f?kw=%E7%94%9F%E6%B4%BB%E5%A4%A7%E7%88%86%E7%82%B8&ie=utf-8'

#设置需要爬取的页面数量

deep=3

if __name__ == '__main__':
    main(base_url,deep)
