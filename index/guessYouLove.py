#coding:utf-8
import MySQLdb

#猜你喜欢模块
def guessLove(name_id):
    #连接数据库
    db = MySQLdb.connect("localhost","root","root","blog_analysic_system")
    cursor = db.cursor()
    #查询当前用户的推荐列表
    # sql1 = "select user_tj_id from all_user_tuijian where user_id = '100'"
    sql1 = "select user_tj_id,cos_value from all_user_tuijian where user_id = "+name_id+" "
    cursor.execute(sql1)
    user_tj={}
    i = 0
    for row in cursor.fetchall():
        if i <10:
            #根据用户的id获取用户名
            sql2 = "select user_name from login_usernum where user_id = "+row[0]+" "
            cursor.execute(sql2)
            for r in cursor.fetchall():
                for j in r:
                    user_tj[j]=row[1]
        i = i+1
    #保证返回的数据是按value降序排列
    user_tj_sort =  sorted(user_tj.iteritems(),key = lambda dic:dic[1],reverse=True)

    username_list = []
    usersim_list = []
    for key,value in user_tj_sort:
        username_list.append(key)
        usersim_list.append(float(value))
    return user_tj_sort,username_list,usersim_list