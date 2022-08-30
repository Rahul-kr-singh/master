# i have create this file -Rks

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # params = {"Name":"Rahul","Place":"Mars"}
    return render(request,'index.html')


def removepunc(request):
    djtext = request.GET.get('text', 'default')
    print(djtext)
    return HttpResponse("remove punc")

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("capitalize first")


def spaceremove(request):
    return HttpResponse("space remover\n <a href ='/'>back</a> ")

def charcount(request):
    return HttpResponse("charcount ")
