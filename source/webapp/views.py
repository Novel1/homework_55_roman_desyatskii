from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404

from webapp.forms import ToDoForm
from webapp.models import ToDo, StatusChoice


# Create your views here.

def index(request):
    return render(request, 'index.html')


def add_task(request):
    if request.method == 'GET':
        form = ToDoForm()
        return render(request, 'add_task.html', context={'choices': StatusChoice.choices, 'form': form})

    form = ToDoForm(data=request.POST)
    if not form.is_valid():
        return render(request, 'add_task.html', context={
            'choices': StatusChoice.choices,
            'form': form,
        })

    else:
        todo_data ={
            'title': request.POST.get('title'),
            'description': request.POST.get('description'),
            'status': request.POST.get('status'),
            'created_at': request.POST.get('created_at'),
        }
        todo = ToDo.objects.create(**todo_data)
        return redirect('inform', pk=todo.pk)


def inform_list(request, pk):
    try:
        todo = ToDo.objects.get(pk=pk)
    except ToDo.DoesNotExist:
        return HttpResponseNotFound('<h1>Not Found</h1>')
    return render(request, 'inform.html', context={
        'todo': todo
    })


def todo_list(request):
    todo = ToDo.objects.exclude(is_deleted=True)
    context = {
        'todo': todo
    }
    return render(request, 'todo_list.html', context=context)


def update_view(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.description = request.POST.get('description')
        todo.status = request.POST.get('status')
        todo.created_at = request.POST.get('data')
        todo.save()
        return redirect('inform', pk=todo.pk)
    return render(request, 'todo_update.html',
                  context={
                      'todo': todo,
                      'choices': StatusChoice.choices
                  })


def confirm_delete(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    if request.method == 'GET':
        return render(request, 'todo_confirm_delete.html', context={'todo': todo})
    elif request.method == 'POST':
        if request.POST.get('exit'):
            return redirect('list')
        else:
            todo.delete()
            return redirect('list')
