from django.shortcuts import render

# Create your views here.

from app.models import *
from django.db.models import Q

def equijoins(request):

    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2024)
    
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(hiredate__year=2024,sal__gt=2500)
    
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno=10)
    
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dname='ACCOUNTING')
    EMPOBJECTS=Emp.objects.select_related('deptno').all()
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(deptno__dlocation='DALLAS')
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(mgr__isnull=True)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=True)
    EMPOBJECTS=Emp.objects.select_related('deptno').filter(comm__isnull=False)
    EMPOBJECTS=Emp.objects.select_related('deptno').all()[2:5:]

    d = {'objects':EMPOBJECTS}
    return render(request,'equijoins.html',d)

def emg_mgr_dept(request):
    emd = Emp.objects.select_related('deptno','mgr').all()
    emd = Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dname = 'research') | Q(deptno = 10))
    emd = Emp.objects.select_related('deptno','mgr').filter(Q(deptno__dlocation = 'dallas') | Q(mgr__ename = 'scott'))
    emd = Emp.objects.select_related('deptno','mgr').filter(mgr__sal__gte = '3000')
    d = {'emd':emd}
    return render(request,'emg_mgr_dept.html',d)