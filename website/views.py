#coding:utf-8
from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response

from website.models import UserInfo
from website.templates.forms import AdduserForm
from website.models import Asset

# Create your views here.


def index(request,kwargs):
    return HttpResponse('index.html')

def index(request):
    return render(request, 'index.html', locals())
def ApplyCertificate(request):
    return  render(request,'ApplyCertificate.html',locals())
def Login(request):
    if request.method == 'POST':
        user = request.POST.get('username',None)
        pwd = request.POST.get('password',None)
        result = UserInfo.objects.filter(user=user,pwd=pwd).count()
        if result == 1:
            return HttpResponse('登陆成功')
        else:
            return render_to_response('login.html',{'status':'用户名或密码错误'})
    else:
        return render_to_response('login.html')
    return HttpResponse('login')
def Adduser(request):
    adduserform = AdduserForm()

    if request.method == 'POST':
        form = AdduserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
        else:
            form.errors
    else:
        return render_to_response('adduser.html', {'form': '用户名存在'})

#数据库操作
#增
def Adddata(request,name):
    Asset.objects.create(hostname=name)
    return HttpResponse('ok')
#删
def Deldata(request,id):
    Asset.objects.get(id=id).delete()
    return HttpResponse('ok')
#改
def Update(request,id,hostname):
    '''
    obj = Asset.objects.get(id=id)
    obj.hostname = hostname
    obj.save()
    '''
    Asset.objects.filter(id__gt=id).update(hostname=hostname)
    return HttpResponse('ok')
#查
def Getdata(request,hostname):
    assetList = Asset.objects.filter(hostname__contains=hostname)
    for item in assetList:
        print item.hostname
    return HttpResponse(item.hostname)
