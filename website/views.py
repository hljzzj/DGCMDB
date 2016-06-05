from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.


def index(request,kwargs):
    return HttpResponse('index.html')

def index(request):
    return render(request, 'index.html', locals())