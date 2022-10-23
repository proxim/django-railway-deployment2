from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from deploythis.settings import ENV_VAR

class HomeView(View):
    def get(self, request):
        return render(request, 'index.html', context={'heading_text': ENV_VAR})