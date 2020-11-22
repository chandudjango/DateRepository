from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def datetimeinfo(request):
    date=datetime.datetime.now()
    hr=int(date.strftime("%H"))
    s2='<h1>Hello Guest'
    if hr<12:
        s2=s2+'good mornig'
    elif hr<16:
        s2=s2+'good afternoon'
    elif hr<21:
        s2=s12+'good night'
    elif hr<24:
        s2=s2+'midnight time now:'
    s2=s2+'</h1><hr>'
    s2=s2+'<h1>The current date and time in hour:'+str(date)+' </h1>'
    return HttpResponse(s2)
