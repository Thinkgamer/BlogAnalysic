#coding:utf-8
import MySQLdb

#定义数据库连接函数
def connect():
    #数据库连接
    db = MySQLdb.connect("127.0.0.1","root","root","blog_analysic_system")
    cursor = db.cursor()
    return db,cursor

#数据库关闭
def close(db,cursor):
    db.close()
    cursor.close()

#用户id转化为name
def idTOName(huname_list):
    db,cursor = connect()
    hdname_list = []
    for name in huname_list:
        sql = "select user_name from login_usernum where user_id = "+name+" "
        cursor.execute(sql)
        for row in cursor.fetchall():
            hdname_list.append(row[0])

    close(db,cursor)
    return hdname_list

#丁yui互动分析类
class huDong():
    def __init__(self,user_id):
        self.db = MySQLdb.connect("127.0.0.1","root","root","blog_analysic_system")
        self.cursor = self.db.cursor()
        self.userid = user_id

    #定义互动比例图函数
    def hudongbili(self):
        hd_list1 = []
        hd_list2 = []
        sql1 = "select hd_num,hd_name from hudong_change where user_id = "+self.userid+" and weekday = '7' "
        self.cursor.execute(sql1)
        for row1 in self.cursor.fetchall():
            hd_list1.append(row1[0])
            hd_list1.append(row1[1])


        sql2 = "select focus,fans from message_all_change where user_id = "+self.userid+" and weekday = '7' "
        self.cursor.execute(sql2)
        for row2 in self.cursor.fetchall():
            hd_list2.append(row2[0])
            hd_list2.append(row2[1])

        return hd_list1,hd_list2

    #定义新增互动名单模块函数
    def newAddHuDong(self):
        newAddList = []
        day = 1
        for day in range(1,8):
            sql = "select hd_num from hudong_change where user_id = "+self.userid+" and weekday = "+str(day)+ " "
            self.cursor.execute(sql)
            for row in self.cursor.fetchall():
                newAddList.append(int(row[0]))

        return newAddList

    #定义所有互动名单模块函数
    def allHuDong(self):
        pass

    def close(self):
        self.db.close()
        self.cursor.close()