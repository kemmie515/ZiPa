from django.shortcuts import render
from django.views.generic import TemplateView

class ZipaHome(TemplateView):
    template_name: str = 'index.html'