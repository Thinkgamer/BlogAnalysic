#coding:utf-8
from django.shortcuts import render,HttpResponse,render_to_response,HttpResponseRedirect
# Create your views here.

def change(request):

    return HttpResponseRedirect("login/login")
