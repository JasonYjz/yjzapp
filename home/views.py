# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
 
 
def index(request):
    #return HttpResponse(u"welcome!")
    context = {}
    context['name'] = 'Jason'
    return render(request, 'simple.html', context)
