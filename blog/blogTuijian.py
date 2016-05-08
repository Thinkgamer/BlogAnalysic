#coding:utf-8


import MySQLdb
import urllib2
from bs4 import BeautifulSoup

def down(url):
   try:
       header = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
       response = urllib2.Request(url,headers=header)
       page = urllib2.urlopen(response).read()
   except:
       return "error"

   if  urllib2.urlopen(response).getcode()!= 200:
       return "error"
   return page

def getTitle(url):
    page = down(url)
    if page is None:
        return "error"
    try:
        soup = BeautifulSoup(page,"lxml",from_encoding="utf-8")
    except Exception as e:
        print 'Html_Parser:',e
        try:
            soup = BeautifulSoup(page)
        except:
            return "error"
    div = soup.find("div",{"class":"article_title"})
    title = div.get_text()
    return title

def getContent(url):
    page = down(url)
    if page is None:
        return "error"
    try:
        soup = BeautifulSoup(page,"lxml",from_encoding="utf-8")
    except Exception as e:
        print 'Html_Parser:',e
        try:
            soup = BeautifulSoup(page)
        except:
            return "error"
    div = soup.find("div",{"class":"article_content"})
    content = div.get_text()
    return content

def getHot(id):
    blog_list = []
    db = MySQLdb.connect("127.0.0.1","root","root","blog_analysic_system")
    cursor = db.cursor()
    i = 0
    new_id = id
    while i<1000:
        id = new_id
        sql = "select id2 from blog_tuijian where id1 = "+id+""
        cursor.execute(sql)
        for row in cursor.fetchall():
            # print row[0]
            new_id = row[0]
            sql_1 = "select blog_title from blog_message where blog_id = "+new_id+""
            cursor.execute(sql_1)
            for row_1 in cursor.fetchall():
                blog_list.append(row_1[0])

        i+=1
    return set(blog_list)


class blogTui():
    def __init__(self,name_id):
        self.id = name_id
        self.db = MySQLdb.connect("127.0.0.1","root","root","blog_analysic_system")
        self.cursor = self.db.cursor()
        self.free_idauthor={}
        self.free_idtitle={}

    def show(self):

        sql = "select blog_title,blog_id,user_id from blog_message order by rand() DESC LIMIT 12"
        self.cursor.execute(sql)
        for row in self.cursor.fetchall():
            sql1 = "select user_name from login_usernum where user_id = "+row[2]+""
            self.cursor.execute(sql1)
            for row1 in self.cursor.fetchall():
                name = row1[0]
            self.free_idauthor[row[1]]=name
            self.free_idtitle[row[1]]=row[0]
        return self.free_idauthor,self.free_idtitle

