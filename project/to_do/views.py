from django.shortcuts import render,redirect
from .models import ToDoItems

# Create your views here.


def home(request):
    todos = ToDoItems.objects.all()
    return render(request,'main.html', {'todos':todos})

def adding(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        ToDoItems.objects.create(title=title)
        return redirect('home')

def deleting(request,id):
    todo = ToDoItems.objects.get(id=id)
    todo.delete()
    return redirect('home')

def edit(request,id):
    
    todo = ToDoItems.objects.get(id=id)
    
    if request.method == 'POST':
        new_title = request.POST.get('title')
        todo.title = new_title
        todo.save()
        return redirect('home')
    
    return render(request,'edit.html',{'todo':todo})
