# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	# construct dictionary to pass to the template engine as its context
	context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
	# return rendered response which is sent to client
	return render(request, 'rango/index.html', context=context_dict)

def about(request):
	context_dict = {'boldmessage': 'a cat will appear on this page'}
	return render(request, 'rango/about.html', context=context_dict)
