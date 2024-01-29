from django.contrib import admin

# Register your models here.

from app.models import *

class cust(admin.ModelAdmin):
    list_display = ['deptno','dname','dlocation']


admin.site.register(Dept,cust)

admin.site.register(Emp)

admin.site.register(Salgrade)
