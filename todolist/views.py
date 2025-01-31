from django.shortcuts import render,redirect
from django .http import HttpResponse
from . models import *
from . forms import *

# Create your views here.
def index(request):
    task=Task.objects.all()
    form=TaskForm()
    if request.method=="POST":
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    
    
    context={
        'tasks':task,'form':form,
    }
    return render(request,'todolist\list.html',context)

def update(request,pk):
    task=Task.objects.get(id=pk)
    form=TaskForm(instance=task)
    if request.method=="POST":
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/') 
    context={
        'form':form
    }
    return render(request,'todolist/update.html',context)    

def delete(request,pk):
    item=Task.objects.get(id=pk)
    if request.method=="POST":
        item.delete()
        return redirect('/')    

    context={
        'item':item

    }

    return render(request,'todolist\delete.html',context)