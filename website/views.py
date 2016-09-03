#coding:utf-8
from django.http.response import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response
import chartit
from website.forms import AdduserForm,ApplyCertificateForm,AddServerHostForm,AddWorkGroupForm,AddThreeNetworkForm
from website.models import Asset
from website.models import UserInfo,ApplyCateInfo,ServerHost,ServerHostRecord,WorkGroup,ThreeNetwork,ThreeNetworkRecord


# Create your views here.


def Index(request):
    #index_serverlist = ServerHost.objects.all()
    good_serverlist = ServerHost.objects.filter(status=1)
    bad_serverlist = ServerHost.objects.filter(status=2)
    return render_to_response('index.html',{'goodserver':good_serverlist,'badserver':bad_serverlist})
def ApplyCertificate(request):
    applycertificateForm = ApplyCertificateForm()
    if request.method == 'POST':
        form = ApplyCertificateForm(request.POST)
        if form.is_valid():
            applytype = request.POST.get('ApplyType',)
            username = request.POST.get('UserName')
            result = ApplyCateInfo.objects.filter(UserName=username).count()
            if result == 0:
                ApplyCateInfo.objects.create(username=username)
        else:
            return render_to_response('ApplyCertificate.html',{'form':applycertificateForm})
    else:
        return render_to_response('ApplyCertificate.html',{'form':applycertificateForm})

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
            username = request.POST.get('username',None)
            email = request.POST.get('email',None)
            result = UserInfo.objects.filter(user=username).count()
            if result == 0:
                UserInfo.objects.create(user=username,pwd=email)
            else:
                return render_to_response('adduser.html', {'form': adduserform,'status':'用户名存在'})
        else:
            temp = form.errors.as_data()
            print temp['email'][0].messages[0]
    return render_to_response('adduser.html', {'form': adduserform})

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

def AssetList(request):
    asset_list = Asset.objects.all()
    return render_to_response('assetlist.html',{'data':asset_list})

#运维功能
def ServerHostList(request):
    serverhost_list = ServerHost.objects.all()
    return render_to_response('ServerHostList.html',{'serverhostlist':serverhost_list})

def ServerHostID(request,hostID):
    hostidsend = ServerHostRecord.objects.filter(hostIP_id=hostID).count()
    hostidstart = hostidsend -  100
    serverhost_id = ServerHostRecord.objects.filter(hostIP_id=hostID).order_by('-id')[0:100]
    serverhost_name = ServerHost.objects.filter(id=hostID)

    return render_to_response('ServerHost.html',{'serverhostnamedata':serverhost_name,'serverhostdata':serverhost_id})

def AddServerHost(request):
    addserverhostForm = AddServerHostForm()
    if request.method == 'POST':
        form = AddServerHostForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name',None)
            ip = request.POST.get('ip',None)
            result1 = ServerHost.objects.filter(hostName=name).count()
            result2 = ServerHost.objects.filter(hostIP=ip).count()
            if result1 == 0 and result2 == 0:
                ServerHost.objects.create(hostName=name,hostIP=ip)
                return render_to_response('AddServerHost.html', {'form': addserverhostForm, 'status': '添加成功'})
            elif result1 != 0:
                return render_to_response('AddServerHost.html', {'form': addserverhostForm,'status':'主机名存在'})
            else:
                return render_to_response('AddServerHost.html', {'form': addserverhostForm, 'status': 'IP已存在'})
        else:
            temp = form.errors.as_data()
            print temp['ip'][0].messages[0]
    return render_to_response('AddServerHost.html', {'form': addserverhostForm})

def AddWorkGroup(request):
    addworkgroupForm = AddWorkGroupForm()
    workgroup_list = WorkGroup.objects.all()
    if request.method == 'POST':
        form = AddWorkGroupForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name',None)
            result1 = WorkGroup.objects.filter(name=name).count()
            if result1 == 0:
                WorkGroup.objects.create(name=name)
                return render_to_response('AddWorkGroup.html', {'form': addworkgroupForm, 'status': '添加成功','workgrouplist': workgroup_list})
            elif result1 != 0:
                return render_to_response('AddWorkGroup.html', {'form': addworkgroupForm,'status':'部门名存在','workgrouplist': workgroup_list})
            else:
                return render_to_response('AddWorkGroup.html', {'form': addworkgroupForm, 'status': 'IP已存在','workgrouplist': workgroup_list})
    return render_to_response('AddWorkGroup.html', {'form': addworkgroupForm,'workgrouplist': workgroup_list})

def AddThreeNetwork(request):
    addthreenetworkForm = AddThreeNetworkForm()
    threenetwork_list = ThreeNetwork.objects.all()
    workgroup_list = WorkGroup.objects.all()
    if request.method == 'POST':
        form = AddThreeNetworkForm(request.POST)
        if form.is_valid():
            vlan = request.POST.get('vlan',None)
            gateway = request.POST.get('gateway',None)
            netmask = request.POST.get('netmask',None)
            workgroupID = request.POST.get('workgroup',None)
            result1 = ThreeNetwork.objects.filter(vlan=vlan).count()
            result2 = ThreeNetwork.objects.filter(gateway=gateway).count()
            result3 = ThreeNetwork.objects.filter(workgroupID=workgroupID).count()
            print workgroupID
            if result1 == 0 and result2 == 0 and result3 ==0:
                ThreeNetwork.objects.create(vlan=vlan,gateway=gateway,netmask=netmask,workgroupID_id=workgroupID)
                return render_to_response('AddThreeNetwork.html', {'form': addthreenetworkForm, 'status': '添加成功','threenetworklist': threenetwork_list,'workgrouplist':workgroup_list})
            elif result1 != 0:
                return render_to_response('AddThreeNetwork.html', {'form': addthreenetworkForm,'status':'VLAN已存在','threenetworklist': threenetwork_list,'workgrouplist':workgroup_list})
            elif result2 != 0:
                return render_to_response('AddThreeNetwork.html', {'form': addthreenetworkForm, 'status': '网关已存在','threenetworklist': threenetwork_list,'workgrouplist':workgroup_list})
            else:
                return render_to_response('AddThreeNetwork.html', {'form': addthreenetworkForm, 'status': '该部门已存在',
                                                                   'threenetworklist': threenetwork_list,
                                                                   'workgrouplist': workgroup_list})
        else:
            print form
            temp = form.errors.as_data()
            print temp
    return render_to_response('AddThreeNetwork.html', {'form': addthreenetworkForm,'threenetworklist': threenetwork_list,'workgrouplist':workgroup_list})

def ThreeNetworkID(request,threenetworkID):
    #threenetwork_id = ThreeNetworkRecord.objects.filter(hostIP_id=hostID)
    threenetwork_name = ThreeNetworkRecord.objects.filter(id=threenetworkID)
    return render_to_response('ThreeNetwork.html',{'threenetworkdata':threenetwork_name})
