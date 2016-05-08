#coding:utf-8

import MySQLdb

class guiDang():
    def __init__(self,name_id):
        self.id = name_id
        self.db = MySQLdb.connect("127.0.0.1","root","root","blog_analysic_system")
        self.cursor = self.db.cursor()
        self.pv_list = []
        self.jifen_list = []
        self.dis_list = []

    #获取日访问量，日积分，日评论
    def get(self):
        day = 1
        for day in range(1,8):
            sql = "select pv_add,jifen_add,pinglun_add from message_change where user_id = "+self.id+" and weekday = "+str(day)+" "
            self.cursor.execute(sql)
            for row in self.cursor.fetchall():
                self.pv_list.append(int(row[0]))
                self.jifen_list.append(int(row[1]))
                self.dis_list.append(int(row[2]))

        return self.pv_list,self.jifen_list,self.dis_list

    def close(self):
        self.db.commit()
        self.cursor.close()
        self.db.close()