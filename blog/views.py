import importlib
from django.shortcuts import render
from django.http import response, HttpResponseRedirect, HttpResponseNotFound, HttpResponse
from django.urls import reverse
from django.template.loader import render_to_string

def index(request):
    return render(request,'blog/index.html')
