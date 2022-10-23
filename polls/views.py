from django.shortcuts import render
from django.http import HttpResponse
from deploythis.settings import ENV_VAR

def index(request):
    return HttpResponse(ENV_VAR)