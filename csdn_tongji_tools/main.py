#-*-coding:utf-8-*-
from url_manage import *
from html_parser import *
from send_email import *
from write_mysql import *
import time

#获取具体的每篇博客信息
def get_every_blog_mess(root_url):
    all_blog_url_list = get_all_url(root_url)
    mess_list = get_all_mess(all_blog_url_list)
    return mess_list

#获取总的信息
def get_count_mess(root_url,id):
    me_mess = get_me_mess(root_url,id)
    #写进文件
    write_me_mess(me_mess)
    return me_mess

if __name__=="__main__":
    # user_name = input("请输入你的CSDN博客用户名：")
    user_name = "gamer_gyt"
    root_url = "http://blog.csdn.net/" + user_name
    id = 1
    me_mess_list = []
    # if time.localtime().tm_hour == 23 or time.localtime().tm_hour == 0:
    while True:
        # mess_list = get_every_blog_mess(root_url)
        me_mess = get_count_mess(root_url,id)
        me_mess_list.append(me_mess)
        send_email(me_mess_list,id)
        id += 1
        #一天运行一次
        time.sleep(1*60*10)



