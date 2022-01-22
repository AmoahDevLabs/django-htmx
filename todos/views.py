from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import Todo
from .todo import todos


def todos_list(request):
    todos = Todo.objects.all()
    return render(request, 'todo/todos.html', {'todos': todos})


@require_http_methods(['POST'])
def add_todo(request):
    todo = None
    title = request.POST.get('title', '')
    if title:
        todo = Todo.objects.create(title=title)

    return render(request, 'todo/partials/todo.html', {'todo': todo})


@require_http_methods(['PUT'])
def update_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.is_done = True
    todo.save()
    return render(request, 'todo/partials/todo.html', {'todo': todo})


@require_http_methods(['DELETE'])
def delete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()

    return HttpResponse()


def search(request):
    res_todos = []
    search_query = request.POST['search']
    if len(search_query) == 0:
        return render(request, 'todo/todo.html', {'todos': []})
    for i in todos:
        if search_query in i['title']:
            res_todos.append(i)
    return render(request, 'todo/todo.html', {'todos': res_todos})
