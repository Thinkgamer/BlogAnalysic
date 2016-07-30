#-*-coding:utf-8-*-
import MySQLdb

#数据库连接
def connect():
    db = MySQLdb.connect("127.0.0.1","root","root","blog_analysic_system",charset='gbk')
    cursor = db.cursor()
    return db,cursor

#数据库关闭
def close():
    pass


#得到热门作者
def getHotAuthor():
    author_list = {}
    #连接数据库
    db,cursor = connect()
    sql1 = "select * from all_user_sort"
    cursor.execute(sql1)
    i = 0
    for row in cursor.fetchall():
        if i <10:
            #根据用户的id获取用户名
            sql2 = "select user_name from login_usernum where user_id = "+row[0]+" "
            cursor.execute(sql2)
            for r in cursor.fetchall():
                for j in r:
                    author_list[j]=row[1]
        i = i+1
    #保证返回的数据是按value降序排列
    user_tj_sort =  sorted(author_list.iteritems(),key = lambda dic:dic[1],reverse=True)
    return user_tj_sort

#得到热门博客
def getHotBlog():
    blog_dic={}
    db,cursor = connect()
    sql = "select user_id,blog_title,blog_id,blog_pv from blog_message order by blog_pv DESC LIMIT 10"
    cursor.execute(sql)
    for row in cursor.fetchall():
        #根据用户的id获取用户名
        sql2 = "select user_name from login_usernum where user_id = "+row[0]+" "
        cursor.execute(sql2)
        for row2 in cursor.fetchall():
            name = row2[0]
        href = name + "/article/details/" + row[2]
        blog_dic[row[3]]={href:row[1]}

    return sorted(blog_dic.iteritems(),key = lambda dic:dic[0],reverse=True)

    # return blog_list