from django.contrib import admin

# Register your models here.

from app.models import *

class cust(admin.ModelAdmin):
    list_display = ['deptno','dname','dlocation']

class cust2(admin.ModelAdmin):
    list_display = ['empno','ename','job','mgr','hiredate','sal','comm','deptno']

admin.site.register(Dept,cust)

admin.site.register(Emp,cust2)

admin.site.register(Salgrade)
