#coding:utf-8
from django.db import models

# Create your models here.

class UserNum(models.Model):
    user_name = models.CharField(max_length=20,verbose_name='用户名')
    user_id = models.CharField(max_length=20,verbose_name='用户ID')

class User(models.Model):
    user_id = models.CharField(max_length=20,verbose_name='用户')
    user_viewnum=models.CharField(max_length=100,verbose_name='访问总量')
    user_jifen = models.CharField(max_length=100,verbose_name='所有积分')
    user_blognum = models.CharField(max_length=100,verbose_name='博客总数')
    user_fromnum = models.IntegerField(verbose_name='转载数目')
    user_fanyinum = models.IntegerField(verbose_name='疑问数目')
    user_disnum = models.IntegerField(verbose_name='评论数目')
    user_focusnum = models.IntegerField(verbose_name='关注人数')
    user_fansnum = models.IntegerField(verbose_name='粉丝人数')
    user_focusid = models.TextField(verbose_name='关注列表')
    user_fansid = models.TextField(verbose_name='粉丝列表')

    class Meta:
        db_table = 'userMessage'

    def __uncode__(self):
        return self.user_name