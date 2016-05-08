#coding:utf-8
from django.shortcuts import render,HttpResponse,render_to_response
import getHot as gh

# Create your views here.
def see(request):
    #得到热门作者
    author_list = gh.getHotAuthor()

    #得到热门博客
    blog_dic = gh.getHotBlog()

    return render_to_response("see.html",{
        "author_list":author_list,
        "blog_dic":blog_dic,
    })