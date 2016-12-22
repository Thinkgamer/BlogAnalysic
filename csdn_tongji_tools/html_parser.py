#-*-coding:utf-8-*-
import urllib.request
from bs4 import BeautifulSoup
import time

def getPage(href):  # 伪装成浏览器登陆,获取网页源代码
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
    }
    req = urllib.request.Request(
        url=href,
        headers=headers
    )
    if urllib.request.urlopen(req).read():
        return BeautifulSoup(urllib.request.urlopen(req).read())

#获取总共有多少页
def get_page_number(url):
    page = getPage(url)
    return int(page.find("div",class_="pagelist").span.get_text().strip().split("  ")[1][1:-1])

#获取每页的博客链接
def get_one_page_url(url):
    url_list = []
    page = getPage(url)
    span_list = page.find_all("span",class_="link_view")
    for span in span_list:
        url_list.append("http://blog.csdn.net/"+span.a.get("href"))
    return url_list

#获取每篇博客的访问信息
def get_all_mess(url_list):
    mess_list = []
    for url in url_list:
        mess_dic = {}
        page = getPage(url)
        blog_id= url.split("/")[-1]
        publish_time=page.find("span",class_="link_postdate").get_text()
        see_num=int(page.find("span",class_="link_view").get_text()[:-3])
        dis_num=page.find("span",class_="link_comments").get_text().split("(")[1][:-1]
        mess_dic["blog_id"]=blog_id
        mess_dic["blog_mess"]={"publish_time":publish_time,"dis_num":dis_num,"see_num":see_num}
        mess_list.append(mess_dic)
    return mess_list

#获取自己信息
def get_me_mess(root_url,id):
    page = getPage(root_url)
    i = 0
    me_dic = {}
    _dic = {}
    for li in page.find("ul",id="blog_rank").find_all("li"):
        if i==0:
            _dic["see_num"]=li.get_text().split("：")[1][:-1]
        elif i == 1:
            _dic["jifen"]=li.get_text().split("：")[1]
        elif i ==3:
            _dic["paiming"] =li.get_text().split("：")[1][1:-1]
        else:
            pass
        i += 1
    j = 0
    for li in page.find("ul",id="blog_statistics").find_all("li"):
        if j==0:
            _dic["yuanchuang"] = int(li.get_text().split("：")[1][:-1])
        elif j ==1:
            _dic["zhuanzai"] = int(li.get_text().split("：")[1][:-1])
        elif j== 2:
            _dic["fanyi"] = int(li.get_text().split("：")[1][:-1])
        elif j == 3:
            _dic["pinglun"] = int(li.get_text().split("：")[1][:-1])
        else:
            pass
        j+=1
    _dic["name"]=root_url.split("/")[-1]
    _dic["time"] = time.strftime("%Y-%m-%d")
    me_dic["me_mess"] = _dic
    me_dic["id"] = id
    return me_dic
