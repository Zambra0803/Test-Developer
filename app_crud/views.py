from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task
# Create your views here.

def crear_listar_tarea(request):

    tasks = Task.objects.all()

    if request.method == 'POST':

        form = TaskForm(request.POST)
        form.save()    

        return render(request, 'index.html', {
            'form': TaskForm,
            'tasks': tasks
        })

    else:
        return render(request, 'index.html', {
            'form': TaskForm,
            'tasks': tasks
        })

def eliminar_tarea(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('crear_listar_tarea')

def editar_tarea(request, id):
    if request.method == 'GET':
        task = Task.objects.get(id=id)
        form = TaskForm(instance=task)
        return render(request, 'editar_tarea.html', {
            'form': form,
            'task': task
        })
    else:
        task = Task.objects.get(id=id)
        new_task = TaskForm(request.POST, instance=task)
        new_task.save()
        return redirect('crear_listar_tarea')


