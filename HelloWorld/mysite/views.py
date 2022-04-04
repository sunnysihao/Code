from django.shortcuts import render

from django.http import HttpResponse

def hello(requrst):
    return HttpResponse("hello world")
