from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

@login_required(login_url='/admin/login/')
def index(request):
    template = loader.get_template('graph/index.html')
    return HttpResponse(template.render({}, request))

@login_required(login_url='/admin/login/')
def graph(request):
    template = loader.get_template('graph/graph.html')
    return HttpResponse(template.render({}, request))
