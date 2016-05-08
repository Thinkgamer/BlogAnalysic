#coding:utf-8
import MySQLdb

#定义关注模块数据类
class Focus():
    def __init__(self,name_id):
        self.db = MySQLdb.connect("127.0.0.1","root","root","blog_analysic_system")
        self.cursor = self.db.cursor()
        self.id = name_id
        self.focusAllNum = []
        self.focusAllNameId = []
        self.focusNewAddNum_list = []

    #获得所有关注人数,粉丝人数
    def getAllFocusName(self):
        day = 1
        for day in range(1,8):
            sql ="select focus,focusname from message_all_change where user_id = "+self.id+" and weekday = "+str(day)+" "
            self.cursor.execute(sql)
            for row in self.cursor.fetchall():
                self.focusAllNum.append(int(row[0]))
            if day == 7:
                self.focusAllNameId.append(row[1])

        # print self.focusAllNameId
        return self.focusAllNum,self.focusAllNameId

    #获得新增关注数目
    def getNewAddFocusNum(self):
        day = 1
        for day in range(1,8):
            sql = "select focusnum_add from message_change where user_id = "+self.id+" and weekday = "+str(day)+" "
            self.cursor.execute(sql)
            for row in self.cursor.fetchall():
                self.focusNewAddNum_list.append(int(row[0]))

        return self.focusNewAddNum_list


    def close(self):
        self.db.close()
        self.cursor.close()