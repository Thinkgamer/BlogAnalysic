#-*-coding:utf-8-*-
from html_parser import *
import numpy
def get_all_url(url):
    url_list =[]
    # page_num =  get_page_number(url)   #得到总共有多少页
    page_num = 11
    for i in range(page_num):
        url = "http://blog.csdn.net/Gamer_gyt/article/list/"+str(i+1)
        url_list += get_one_page_url(url)
    return set(url_list)