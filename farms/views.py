from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def index(request):
    response = "The farmer has id %s"
    template = loader.get_template('farms/index.html')
    return HttpResponse(template.render({}, request))


# Create your views here.
