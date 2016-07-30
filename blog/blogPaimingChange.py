#coding:utf-8

import MySQLdb

class blogPaiming():
    def __init__(self,name_id):
        self.id = name_id
        self.db = MySQLdb.connect("127.0.0.1","root","root","blog_analysic_system",charset='gbk')
        self.cursor = self.db.cursor()
        self.pvSort_dic = {}
        self.disSort_dic = {}
        self.disSort_idDic={}
        self.timeSort_dic={}

    #返回pv排名的博客字典
    def pvSort(self):
        sql = "select blog_title,blog_id,blog_pv from blog_message where user_id = "+self.id+" order by blog_pv DESC LIMIT 10"
        self.cursor.execute(sql)
        for row in self.cursor.fetchall():
            self.pvSort_dic[row[2]]={row[0]:row[1]}
        return sorted(self.pvSort_dic.iteritems(),key = lambda dic:dic[0],reverse=True)

    #返回dis排名的博客字典,#注意不能将评论量作为key，因为其不唯一
    def disSort(self):
        sql = "select blog_title,blog_id,blog_dis from blog_message where user_id = "+self.id+" order by blog_dis DESC LIMIT 10"
        self.cursor.execute(sql)
        for row in self.cursor.fetchall():
            self.disSort_dic[row[1]]=row[2]
            self.disSort_idDic[row[1]]=row[0]
            # print self.disSort_dic[row[1]][row[0]]
        return sorted(self.disSort_idDic.iteritems(),key = lambda dic:dic[1],reverse=True),sorted(self.disSort_dic.iteritems(),key = lambda dic:dic[1],reverse=True)

    def timeSort(self):
        sql = "select blog_title,blog_id,blog_time from blog_message where user_id = "+self.id+" order by blog_time DESC LIMIT 10"
        self.cursor.execute(sql)
        for row in self.cursor.fetchall():
            self.timeSort_dic[row[2][:10]]={row[0]:row[1]}
        self.timeSort_dic=sorted(self.timeSort_dic.iteritems(),key = lambda dic:dic[0],reverse=True)
        return self.timeSort_dic

    def close(self):
        self.db.commit()
        self.cursor.close()
        self.db.close()
