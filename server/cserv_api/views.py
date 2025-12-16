from django.shortcuts import render
from django.http import HttpResponse
from pycserv import *

def number(request):
    return HttpResponse(func())
