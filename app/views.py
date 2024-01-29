from django.shortcuts import render

# Create your views here.

from app.models import *

def equijoins(request):
    objects = Emp.objects.select_related('deptno').all()
    d = {'objects':objects}
    return render(request,'equijoins.html',d)