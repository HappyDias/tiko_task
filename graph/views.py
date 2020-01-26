from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def index(request):
    template = loader.get_template('graph/index.html')
    return HttpResponse(template.render({}, request))

def graph(request):
    template = loader.get_template('graph/graph.html')
    return HttpResponse(template.render({}, request))
