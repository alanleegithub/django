from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hello world %s %s %s" % (request.path, request.get_host(), request.get_full_path()))

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

import datetime
def current_datetime(request):
    now = datetime.datetime.now()
    return render(request, 'current_datetime.html', {'current_date': now})
    #t = get_template("current_datetime.html")
    #html = t.render(Context({'current_date': now}))
    #return HttpResponse(html)
