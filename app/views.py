from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from app.forms import *
from django.http import HttpResponse
# Create your views here.

class temp(TemplateView):
    template_name='temp_page.html'


class student(TemplateView):
    template_name='student.html'
    def get_context_data(self, **kwargs):
        ECDO = super().get_context_data(**kwargs)
        # ECDO['name']='hari'
        SFO=StudentForms()
        ECDO['SFO']=SFO
        return ECDO
    
    def post(self,request):
        SFDO=StudentForms(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('data inserted')
        