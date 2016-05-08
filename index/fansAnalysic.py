#coding:utf-8
import MySQLdb

#定义关注模块数据类
class Fans():
    def __init__(self,name_id):
        self.db = MySQLdb.connect("127.0.0.1","root","root","blog_analysic_system")
        self.cursor = self.db.cursor()
        self.id = name_id
        self.fansAllNum = []
        self.fansAllNameId = []
        self.fansNewAddNum_list=[]

    #获得所有关注人数,粉丝人数
    def getAllFansName(self):
        day = 1
        for day in range(1,8):
            sql ="select fans,fansname from message_all_change where user_id = "+self.id+" and weekday = "+str(day)+" "
            self.cursor.execute(sql)
            for row in self.cursor.fetchall():
                self.fansAllNum.append(int(row[0]))
            if day == 7:
                self.fansAllNameId.append(row[1])

        return self.fansAllNum,self.fansAllNameId

    #获得新增粉丝数目
    def getNewAddFansNum(self):
        day = 1
        for day in range(1,8):
            sql = "select fansnum_add from message_change where user_id = "+self.id+" and weekday = "+str(day)+" "
            self.cursor.execute(sql)
            for row in self.cursor.fetchall():
                self.fansNewAddNum_list.append(int(row[0]))

        return self.fansNewAddNum_list


    def close(self):
        self.db.close()
        self.cursor.close()