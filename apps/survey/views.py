# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index (request):
    return render (request, 'survey/index.html')

def process (request):
    
    if 'redirects' not in request.session:
        request.session['redirects'] = 1
    else:
        request.session['redirects'] += 1
    print '////////////', request.POST['name']
    request.session['name']= request.POST['name'],
    request.session['location']= request.POST['dojo_location'],
    request.session['fav_lang']= request.POST['fav_lang'],
    request.session['comment']= request.POST['comment']
    
    print request.session['name']
    return redirect ('/result')

def result (request):
    return render (request, 'survey/result.html')

def reset (request):
    request.session.clear()
    print '-----> SESSION HAS BEEN CLEARED!'
    return redirect ('/')