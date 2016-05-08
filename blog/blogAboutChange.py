#coding:utf-8
import MySQLdb

class blogAbout():

    def __init__(self,name_id):
        self.id = name_id
        self.db = MySQLdb.connect("127.0.0.1","root","root","blog_analysic_system")
        self.cursor = self.db.cursor()
        self.yc_num = 0
        self.zz_num = 0
        self.yw_num = 0
        self.blogAdd_list = []

    #获取一周博客新增变化
    def get(self):
        day = 1
        for day in range(1,8):
            sql = "select blog_add,zhuanzai_add,yiwen_add from message_change where user_id = "+self.id+" and weekday = "+str(day)+" "
            self.cursor.execute(sql)
            for row in self.cursor.fetchall():
                self.blogAdd_list.append(int(row[0]) + int(row[1]) + int(row[2]))

        return self.blogAdd_list

    def getThree(self):
        sql = "select blog,zhuanzai,yiwen from message_all_change where user_id = "+self.id+" and weekday = "+str(7)+" "
        self.cursor.execute(sql)
        for row in self.cursor.fetchall():
            self.yc_num = int(row[0])
            self.zz_num =int(row[1])
            self.yw_num = int(row[2])
        return self.yc_num,self.zz_num,self.yw_num