#-*-coding:utf-8-*-
import pymysql

def write_me_mess(mess):
    # try:
    #     # 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
    #     conn = pymysql.connect(host='192.168.1.189', user='root', passwd='123456', db='csdn', port=3306, charset='utf8')
    #     cur = conn.cursor()  # 获取一个游标
    #     sql = "insert into me_mess (time,name,see_num,jifen,paiming) values(%s,%s,%s,%s,%s)"
    #     cur.execute(sql,(mess["time_id"],mess["me_mess"]["name"],mess["me_mess"]["see_num"],mess["me_mess"]["jifen"],mess["me_mess"]["paiming"]))
    #     cur.close()  # 关闭游标
    #     conn.close()
    #     print("write ok")
    # except Exception as e:
    #     print(e)
    with open("me_mess.csv","a") as fw:
        fw.write(mess["me_mess"]["time"]+","+mess["me_mess"]["name"]+","+mess["me_mess"]["see_num"]+","+mess["me_mess"]["jifen"]+","+mess["me_mess"]["paiming"]+"\n")