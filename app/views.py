# from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import loader

# from .models import
# Create your views here.
def index(request):
    sites_list = [{'href':'#proyect','name':'Proyecto'},{'href':'#about','name':'Acerca de'},{'href':'#contact','name':'Contacto'},{'href':'/login','name':'Ingresar'},{'href':'/register','name':'Registrarse'}]#Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
    context = {
        'sites_list': sites_list,
    }
    return HttpResponse(template.render(context, request))
    # return render_to_response('index.html');
def login(request):
    sites_list = []#[{'href':'/login','name':'Ingresar'}]#Question.objects.order_by('-pub_date')[:5]
    # sites_list = [{'href':'/#proyect','name':'Proyecto'},{'href':'/#about','name':'Acerca de'},{'href':'/#contact','name':'Contacto'},{'href':'/login','name':'Ingresar'}]#Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('login.html')
    context = {
        'sites_list': sites_list,
        # 'USER':{'NAME':'José Axpuac'},
    }
    return HttpResponse(template.render(context, request))
    # return render_to_response('login.html');
def register(request):
    sites_list = []#[{'href':'/login','name':'Ingresar'}]#Question.objects.order_by('-pub_date')[:5]
    # sites_list = [{'href':'/#proyect','name':'Proyecto'},{'href':'/#about','name':'Acerca de'},{'href':'/#contact','name':'Contacto'},{'href':'/login','name':'Ingresar'}]#Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('register.html')
    context = {
        'sites_list': sites_list,
        # 'USER':{'NAME':'José Axpuac'},
    }
    return HttpResponse(template.render(context, request))
    # return render_to_response('login.html');
# proyect
# about
# contact
# login