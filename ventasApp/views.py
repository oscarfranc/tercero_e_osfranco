from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Task
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegisterForm
#from django.template import loader

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'usuario {username} creado')
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = { 'form' : form }
    return render(request, 'registration/registro.html', context)

def login(request):
    return render(request,'inicio.html')

@login_required
def inicio(request):
    #template = loader.get_template("inicio.html")
    db_data = Task.objects.all()
    context = {
        "db_data": db_data[::-1],
        "update": None
    }
    #return HttpResponse(template.render(context, request))
    return render(request, "inicio.html", context)

@login_required
def insert(request):
    try:
        task_subject = request.POST["subject"]
        task_description = request.POST["description"]
        if task_subject == "" or task_description == "":
            raise ValueError("No se permite el campo vacio")
        db_data = Task(subject=task_subject, description=task_description)
        db_data.save()
        return HttpResponseRedirect(reverse("inicio"))
    except ValueError as err:
        print(err)
        return HttpResponseRedirect(reverse("inicio"))
    
@login_required
def update(request):
    task_id = request.POST["id"]
    task_subject = request.POST["subject"]
    task_description = request.POST["description"]
    db_data = Task.objects.get(pk=task_id)
    db_data.subject = task_subject
    db_data.description = task_description
    db_data.save()
    return HttpResponseRedirect(reverse("inicio"))
    
@login_required
def update_form(request, task_id):
    db_data = Task.objects.all()
    db_data_only = Task.objects.get(pk=task_id)
    print(db_data_only)
    context = {
        "db_data": db_data[::-1],
        "update": db_data_only
    }
    return render(request, "inicio.html", context)
    
@login_required
def delete(request, task_id):
    db_data = Task.objects.filter(id=task_id)
    db_data.delete()
    return HttpResponseRedirect(reverse("inicio"))
