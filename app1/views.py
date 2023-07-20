from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def My_Name(request):
    return HttpResponse('<h1><marquee>Dhruba Sundar Panda</marquee></h1>')
def Branch(request):
    return HttpResponse('<h1><marquee>Mechanical Engg</marquee></h1>')