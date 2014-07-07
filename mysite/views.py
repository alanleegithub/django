from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render
def hello(request):
    return HttpResponse("Hello world")

import datetime
def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})
    #t = get_template("current_datetime.html")
    #html = t.render(Context({'current_date': now}))
    #return HttpResponse(html)