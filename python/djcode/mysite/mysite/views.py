#!/usr/bin/env python3

from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import datetime
from django.shortcuts import render_to_response



def hello(request):
    return HttpResponse("Hello world")


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)


# def datetime2(request):
#     now = datetime.datetime.now()
#     # t = get_template('mytemplate.html')
#     # html = t.render({'current_date': now})
#     # return HttpResponse(html)
#     return render_to_response('mytemplate.html', {'current_date': now})


def datetime2(request):
    current_date = datetime.datetime.now()
    return render_to_response('current_datetime.html', locals())
