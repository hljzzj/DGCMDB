#coding:utf-8

from django import forms

class AdduserForm(forms.Form):
    username = forms.CharField()
    password = forms.PasswordInput()