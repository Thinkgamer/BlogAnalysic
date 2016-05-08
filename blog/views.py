#coding:utf-8
from django.shortcuts import render,HttpResponseRedirect,render_to_response
from login.models import UserNum
import guiDangChange as gd
import blogAboutChange as ba
import blogPaimingChange as bp
import blogTuijian as btj
# Create your views here.

#博客概况
def blog(request,name):
    #获取当前用户对应的id号
    name_id = UserNum.objects.get(user_name=name).user_id

    #获取日博客撰写和博客每个类别数目
    one = ba.blogAbout(name_id)
    blogAdd_list = one.get()

    bcy,bzz,byw = one.getThree()


    return render_to_response("blog.html",{
        "name":name,
        "blogAdd_list":blogAdd_list,
        "maxbadd":max(blogAdd_list),
        "bcy":bcy,
        "bzz":bzz,
        "byw":byw,
    })

#归档统计变化
def guidang(request,name):
    #获取当前用户对应的id号
    name_id = UserNum.objects.get(user_name=name).user_id

    #获取日pv变化,日积分，日评论
    one = gd.guiDang(name_id)
    pv_list,jifen_list,dis_list = one.get()

    #关闭数据库
    one.close()
    return render_to_response("guidang.html",{
        "name":name,
        "pv_list":pv_list,
        "maxpv":max(pv_list),
        "jifen_list":jifen_list,
        "maxjifen":max(jifen_list),
        "dis_list":dis_list,
        "maxdis":max(dis_list),
    })

#博客排名
def paiming(request,name):
    #获取当前用户对应的id号
    name_id = UserNum.objects.get(user_name=name).user_id
    #获取按访问量排名博客
    one = bp.blogPaiming(name_id)
    pv_dic = one.pvSort()

    #获取按评论数排名
    dis_idDic,dis_dic = one.disSort()
    #获取按发表时间排名
    time_dic = one.timeSort()

    return render_to_response("paiming.html",{
        "name":name,
        "pv_dic":pv_dic,
        "dis_dic":dis_dic,
        "time_dic":time_dic,
        "dis_idDic":dis_idDic,
    })

#推荐
def btuijian(request,name):
    #获取当前用户对应的id号
    name_id = UserNum.objects.get(user_name=name).user_id
    #随机显示10篇文章在博客推荐页面供浏览
    one =btj.blogTui(name_id)
    free_idauthor,free_idtitle =one.show()
    return render_to_response("btuijian.html",{
        "name":name,
        "free_idauthor":free_idauthor,
        "free_idtitle":free_idtitle,

    })

def content(request,name,author,id):
    url = "http://blog.csdn.net/%s/article/details/%s" % (author,id)
    title = btj.getTitle(url)
    content = btj.getContent(url)

    #获得当前博客de推荐列表
    tjblog_list = btj.getHot(id)

    return render_to_response("blogone.html",{
        "name":name,
        "title":title,
        "content":content,
        "tjblog_list":tjblog_list,
        "len":len(tjblog_list),
    })