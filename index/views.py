#coding:utf8
from django.shortcuts import render,HttpResponse,render_to_response
from login.models import User,UserNum
import guessYouLove as gyl
import huDongAnalysic as hd
import focusAnalysic as foc
import fansAnalysic as fan
# Create your views here.

def index(request):
    return render_to_response("user.html",{})


#互动分析模块
def user(request,name):
    #获取当前用户对应的id号
    name_id = UserNum.objects.get(user_name=name).user_id

    #获取当前用户的粉丝数，关注数和互动人数
    one = hd.huDong(name_id)
    hd_list1,hd_list2 = one.hudongbili()
    focusnum = hd_list2[0]
    fansnum = hd_list2[1]
    hudongnum = hd_list1[0]
    huname_list = str(hd_list1[1]).split("|")

    #id转化为用户名
    hdname_list = hd.idTOName(huname_list)
    # print focusnum,focusnum,hudongnum,huname_list

    #新增互动
    hd_new_add_list = one.newAddHuDong()
    maxnum = max(hd_new_add_list)
    # print hd_new_add_list
    return render_to_response("user.html",{
        "name":name,
        "focusnum":focusnum,
        "fansnum":fansnum,
        "hudongnum":hudongnum,
        "hdname_list":hdname_list,
        "hd_new_add_list":hd_new_add_list,
        "maxnum":maxnum,
    })

#关注分析模块
def focus(request,name):
    #获取当前用户对应的id号
    name_id = UserNum.objects.get(user_name=name).user_id

    one = foc.Focus(name_id)
    #获得所有关注人数
    focusAllNum,focusAllNameID = one.getAllFocusName()

    #获得新增关注数目
    focusNewAddNum_list = one.getNewAddFocusNum()
    maxnumnew = max(focusNewAddNum_list)
    print focusNewAddNum_list

    #将nameid全部转化为字符串
    focusAllNameID = str(focusAllNameID[0]).split("|")
    focusname_list = hd.idTOName(focusAllNameID)
    # print focusAllNum

    #最大值
    maxnumall = max(focusAllNum)

    return render_to_response("focus.html", {
        "name":name,
        "focusAllNum":focusAllNum,
        "focusname_list":focusname_list,
        "maxnumall":maxnumall,
        "maxnumnew":maxnumnew,
        "focusNewAddNum_list":focusNewAddNum_list
    })

#粉丝分析模块
def fans(request,name):
    #获取当前用户对应的id号
    name_id = UserNum.objects.get(user_name=name).user_id

    one = fan.Fans(name_id)
    #获得所有关注人数
    fansAllNum,fansAllNameID = one.getAllFansName()
    # print fansAllNum

    #获得新增关注人数
    fansNewAddNum_list=one.getNewAddFansNum()
    print fansNewAddNum_list

    #将nameid全部转化为字符串
    fansAllNameID = str(fansAllNameID[0]).split("|")
    fansname_list = hd.idTOName(fansAllNameID)

    return render_to_response("fans.html", {
        "name":name,
        "fansAllNum":fansAllNum,
        "maxnumall":max(fansAllNum),
        "fansname_list":fansname_list,
        "maxnumnew":max(fansNewAddNum_list),
        "fansNewAddNum_list":fansNewAddNum_list,
    })

#为我推荐模块
def tuijian(request,name):
    #获取当前用户对应的id号
    name_id = UserNum.objects.get(user_name=name).user_id

    #获取为我推荐模块的信息
    user_tj,username_list,usersim_list = gyl.guessLove(name_id)
    maxsim = max(usersim_list)

    return render_to_response("tuijian.html", {
        "name":name,
        "user_tj":user_tj,
        "maxsim":maxsim,
        "username_list":username_list,
        "usersim_list":usersim_list,
    })