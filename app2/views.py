from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Language(request):
    return HttpResponse('<h1><marquee>Python</marquee></h1>')
def FrameWork(request):
    return HttpResponse('<h1><marquee>Django</marquee></h1>')


