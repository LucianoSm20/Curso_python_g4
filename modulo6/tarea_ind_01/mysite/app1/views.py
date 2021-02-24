from django.shortcuts import render
from django.template import loader, context
from django.http import HttpResponse
from django.http import HttpResponsePermanentRedirect
from .models import Departamento

# Create your views here.

def inicio(request):
    context = {'ramos': list(Departamento.objects.values())} 
    return render(request, 'app1/index.html', context)