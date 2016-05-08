from django.contrib import admin
from login.models import User,UserNum
# Register your models here.

class userNumAdmin(admin.ModelAdmin):
    list_display = ('user_name','user_id',)
    ordering = ('user_id',)

admin.site.register(UserNum,userNumAdmin)

class userAdmin(admin.ModelAdmin):
    list_display = ('user_id','user_viewnum','user_jifen','user_blognum','user_fromnum','user_fanyinum', \
                    'user_disnum','user_focusnum','user_fansnum','user_focusid','user_fansid',)
    ordering = ('user_id',)

admin.site.register(User,userAdmin)