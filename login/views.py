#coding:utf-8
from django.shortcuts import render,HttpResponse,render_to_response,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from login.models import UserNum,User
# Create your views here.

@csrf_exempt
def login(request):
    if request.method=="POST":
        name = request.POST.get('account')
        pwd = request.POST.get('password')
        #判断用户是否在数据库中
        if UserNum.objects.filter(user_name=name):
            return HttpResponseRedirect('/index/user/%s' % name)
        else:
            return render_to_response('login.html',{
                'error':"你所输入的用户不存在,请点击确定查看相关注意事项",
            })

    return render_to_response('login.html', {})

def antion(request):
    author_list = []
    import MySQLdb
    db = MySQLdb.connect("127.0.0.1","root","root","blog_analysic_system")
    cursor = db.cursor()
    sql = "select user_name from login_usernum"
    cursor.execute(sql)
    for row in cursor.fetchall():
        author_list.append(row[0])

    return render_to_response("antion.html",{
        "author_list":author_list,
    })