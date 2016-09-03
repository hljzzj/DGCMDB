#coding:utf-8

from django import forms

class AdduserForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField(required=True,error_messages={'invalid':'邮箱格式错误'})

class ApplyCertificateForm(forms.Form):
    ApplyType = forms.ChoiceField(choices=(('1',"首次申请"),('2',"到期延期"),('3',"损坏丢失补办"),('4',"离职退休注销")),widget=forms.RadioSelect,label='申请类型')
    Workgroup = forms.ChoiceField(choices=(('1',"123"),('2',"456")),widget=forms.Select,label='所属部门')
    UserName = forms.CharField(label='姓名')
    UserSex = forms.CharField(label='性别')
    UserPhone = forms.CharField(max_length=11,label='电话')
    UserIDCard = forms.CharField(max_length=18,label='身份证')
    UserEmail = forms.EmailField(required=True,error_messages={'invalid':'邮箱格式错误'},label='邮箱')
    UserAddress = forms.CharField(label='通信地址')
    Userzhiwu = forms.CharField(label='申请类型')
    UserLeve = forms.CharField(label='职级')
    UserWork = forms.CharField(label='工作岗位')
    UserWrokType = forms.CharField(label='警种')
    UserIP = forms.GenericIPAddressField(protocol='ipv4')

class AddServerHostForm(forms.Form):
    name = forms.CharField(max_length=50)
    ip = forms.GenericIPAddressField(error_messages={'invalid': 'IP地址格式错误'})
class AddWorkGroupForm(forms.Form):
    name = forms.CharField(max_length=50)

class AddThreeNetworkForm(forms.Form):
    vlan = forms.CharField(max_length=5,error_messages={'invalid': 'Vlan错误'})
    netmask = forms.GenericIPAddressField(error_messages={'invalid': 'netmask错误'})
    gateway = forms.GenericIPAddressField(error_messages={'invalid': 'gateway错误'})
    workgroup = forms.CharField(max_length=50,error_messages={'invalid': 'ID错误'})



